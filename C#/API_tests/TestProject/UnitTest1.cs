using System;
using Xunit;
using API_tests.Controllers;
using API_tests.Services;
using API_tests.Models;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace TestProject
{
    public class UnitTest1
    {
        DepartmentsController controller;
        IDepartment service;

        public UnitTest1()
        {
            service = new TestService();
            controller = new DepartmentsController(service);
        }

        [Fact]
        public void GetAllProducts()
        {
            Assert.IsType<OkObjectResult>(controller.Get_all_departments("", "", "", 0, 0));
        }

        [Fact]
        public void GetProductById()
        {
            Assert.IsType<OkObjectResult>(controller.Get_amount(1));
        }

        [Fact]
        public void GetProductById_Error()
        {
            Assert.IsType<NotFoundObjectResult>(controller.Get_amount(10));
        }

        [Fact]
        public void CreateProduct()
        {
            Department product = new Department
            {
                ID = 6,
                Title = "Apple",
                Director_name = "Director Apple",
                Phone_number = "+3805014253698",
                Monthly_budget = 2600,
                Yearly_budget = 68000,
                Website = "https://apple.com"

            };
            Assert.IsType<OkObjectResult>(controller.AddProduct(product));
        }

        [Fact]
        public void CreateProduct_Error()
        {
            Department product = new Department
            {
                ID = 9,
                Title = "App4le",
                Director_name = "Director Apple",
                Phone_number = "+380501425369",
                Monthly_budget = 2600,
                Yearly_budget = 68000,
                Website = "https://apple.com"

            };
            controller.ModelState.AddModelError("Title", "No integer/symbols in string!");
            var result = controller.AddProduct(product);
            Assert.IsType<OkObjectResult>(result);

        }

        [Fact]
        public void DeleteProductById()
        {
            Assert.IsType<OkObjectResult>(controller.DeleteProduct(4));
        }

        [Fact]
        public void DeleteProductById_Error()
        {
            Assert.IsType<NotFoundObjectResult >(controller.DeleteProduct(10));
        }

        [Fact]
        public void EditProduct()
        {
            Department product = new Department
            {
                Title = "Apple",
                Director_name = "Director Apple",
                Phone_number = "+3805014253698",
                Monthly_budget = 2600,
                Yearly_budget = 68000,
                Website = "https://apple.com"
            };
            var result = controller.Put_Department(1, product);
            Assert.IsType<OkObjectResult>(result);
        }

        [Fact]
        public void EditProduct_Error()
        {
            Department product = new Department
            {
                Title = "Apple",
                Director_name = "Director Apple",
                Phone_number = "+3805014253698",
                Monthly_budget = 2600,
                Yearly_budget = 68000,
                Website = "https://apple.com"

            };
            var result = controller.Put_Department(10, product);
            Assert.IsType<NotFoundObjectResult>(result);
        }

        [Fact]
        public void Search()
        {
            Parameters a = new Parameters
            {
                Search = "Hello",
                Sort_by = "ID",
                Sort_type = "asc",
                Limit = 5,
                Offset = 1
            };
            var res = service.GetDepartments(a);
            Assert.Equal(1, res.count);
            Assert.NotEqual(5, res.count);
        }

        [Fact]
        public void Sort()
        {
            Parameters a = new Parameters
            {
                Search = "",
                Sort_by = "ID",
                Sort_type = "desc",
                Limit = 5,
                Offset = 1
            };
            var res = service.GetDepartments(a);
            Assert.Equal(4, res.res[0].ID);
            Assert.NotEqual(1, res.count);
        }

        [Fact]
        public void Limit_Offset()
        {
            Parameters a = new Parameters
            {
                Search = "",
                Sort_by = "",
                Sort_type = "",
                Limit = 3,
                Offset = 2
            };
            var res = service.GetDepartments(a);
            Assert.Equal(4, res.count);
            Assert.NotEqual(0, res.count);
        }
    }
}
