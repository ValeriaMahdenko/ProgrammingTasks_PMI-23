using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using API_Department_orders.Models;
using System.Security.Cryptography;
using API_Department_orders.Response;


namespace API_Department_orders.Services
{
    public interface IDepartment
    {
        public (List<Department> res, int count) GetDepartments( Parameters a);
        public Department GetDepartment(int Id);
        public Department AddDepartment(Department data);
        public Department DeleteDepartment(int Id);
        public Department PutDepartment(int Id, Department data);
    }

    public class DepartmentServices : IDepartment
    {
        private Context DBContext = new Context();
        public DepartmentServices(Context ctx)
        {
            DBContext = ctx;
        }

        public (List<Department> res, int count) GetDepartments(Parameters a)
        {
            QueryParams b = new QueryParams();
            List<Department> lst = new List<Department>();
            if (a.Search != null)
                lst = b.Search(DBContext.Departments.ToList(), a.Search);
            else
                lst = DBContext.Departments.ToList();

            lst = b.Sort(lst, a.Sort_type, a.Sort_by);
            if (a.Limit == null || a.Limit < 1)
                a.Limit = lst.Count;

            if (a.Offset == null || a.Offset < 1)
                a.Offset = 1;
            List<Department> to_return = b.Paginate(lst, a.Offset, a.Limit);
            return (to_return, lst.Count);
        }

        public Department GetDepartment(int Id)
        {
            Department res = DBContext.Departments.FirstOrDefault(x => x.ID == Id);
            return res;
        }

        public Department AddDepartment(Department data)
        {
            try
            {
                DBContext.Departments.Add(data);
                DBContext.SaveChanges();
                return data;
            }
            catch
            {
                return null;
            }
        }

        public Department DeleteDepartment(int id)
        {
            Department res = DBContext.Departments.FirstOrDefault(x => x.ID == id);
            if (res != null)
            {
                DBContext.Departments.Remove(res);
                DBContext.SaveChanges();
                return res;
            }
            return null;
        }

        public Department PutDepartment(int Id, Department data)
        {
            Department res = DBContext.Departments.FirstOrDefault(x => x.ID == Id);
            try
            {
                DBContext.Departments.Remove(res);
                DBContext.Departments.Add(data);
                DBContext.SaveChanges();
                return data;
            }
            catch
            {
                return null;
            }
        }
    }
}