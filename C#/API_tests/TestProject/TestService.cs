using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using API_tests.Services;
using API_tests.Models;

namespace TestProject
{
    class TestService : IDepartment
    {
        private readonly List<Department> departments;
        public TestService()
        {
            departments = new List<Department>()
            {
                new Department
                {
                    ID = 1,
                    Title = "Slack",
                    Director_name = "Slack director",
                    Phone_number = "+380501122333",
                    Monthly_budget = 1000,
                    Yearly_budget = 15000,
                    Website = "https://website1.com/"
                },
                new Department
                {
                    ID = 2,
                    Title = "Hello",
                    Director_name = "Hello director",
                    Phone_number = "+380668899111",
                    Monthly_budget = 3500,
                    Yearly_budget = 150000,
                    Website = "https://website2.com/"
                },
                new Department
                {
                    ID = 3,
                    Title = "Goodbye",
                    Director_name = "Goodbye director",
                    Phone_number = "+380662277555",
                    Monthly_budget = 5000,
                    Yearly_budget = 200000,
                    Website = "https://website3.com/"
                },
                new Department
                {
                    ID = 4,
                    Title = "Yes",
                    Director_name = "Yes director",
                    Phone_number = "+380992266458",
                    Monthly_budget = 4200,
                    Yearly_budget = 168000,
                    Website = "https://website4.com/"
                }
            };
        }

        public (List<Department> res, int count) GetDepartments(Parameters a)
        {
            QueryParams b = new QueryParams();
            List<Department> lst = new List<Department>();
            if (a.Search != null)
                lst = b.Search(departments, a.Search);
            else
                lst = departments;

            lst = b.Sort(lst, a.Sort_type, a.Sort_by);
            if (a.Limit == null || a.Limit < 1)
                a.Limit = lst.Count;

            if (a.Offset == null || a.Offset < 1)
                a.Offset = 1;
            List<Department> to_return = b.Paginate(lst, a.Offset, a.Limit);
            return (to_return, lst.Count);
        }
        public Department AddDepartment(Department to_add)
        {
            if (Check_id(to_add, departments))
            {
                departments.Add(to_add);
                return to_add;
            }
            return null;
        }
        public  Department  DeleteDepartment(int id)
        {
            Department to_remove = departments.FirstOrDefault(order => order.ID == id);
            if (to_remove is null)
                return null;
            departments.Remove(to_remove);
            return  to_remove;
        }
        public Department GetDepartment(int id)
        {
            Department to_show = departments.FirstOrDefault(order => order.ID == id);
            if (to_show is null)
                return null;
            return to_show;
        }
        public  Department PutDepartment(int id, Department el)
        {
            Department to_edit = departments.FirstOrDefault(order => order.ID == id);
            if (to_edit is null)
                return null;
            departments.Remove(to_edit);
            if (Check_id(el, departments))
            {
                departments.Add(el);
                return el;
            }
            return null;
        }

        private bool Check_id(Department el, List<Department> lst)
        {
            foreach (var i in lst)
            {
                if (el.ID == i.ID)
                {
                    return false;
                }
            }
            return true;
        }
    }
}
