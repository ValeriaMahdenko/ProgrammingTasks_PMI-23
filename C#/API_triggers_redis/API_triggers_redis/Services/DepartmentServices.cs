using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using API_triggers_redis.Models;
using System.Security.Cryptography;
using API_triggers_redis.Response;
using API_triggers_redis.Cache;


namespace API_triggers_redis.Services
{
    public interface IDepartment
    {
        public (List<Department> res, int count) GetDepartments(Parameters a);
        public Department GetDepartment(int Id);
        public Department AddDepartment(Department data);
        public Department DeleteDepartment(int Id);
        public Department PutDepartment(int Id, Department data);
    }

    public class DepartmentServices : IDepartment
    {
        private Context DBContext = new Context();
        private readonly IRedisCache _cacheClient;

        public DepartmentServices(Context ctx, IRedisCache cacheClient)
        {
            DBContext = ctx;
            _cacheClient = cacheClient;

        }

        public (List<Department> res, int count) GetDepartments(Parameters a)
        {
            QueryParams b = new QueryParams();
            List<Department> pagedProducts = _cacheClient.GetProducts(a.Search, a.Sort_by, a.Sort_type, a.Offset, a.Limit);

            if (pagedProducts is null)
            {
                _cacheClient.SetProducts(a.Search, a.Sort_by, a.Sort_type, a.Offset, a.Limit, pagedProducts);
            }
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
                _cacheClient.RemoveAllCache();
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
                _cacheClient.RemoveAllCache();
                return res;
            }
            return null;
        }

        public Department PutDepartment(int Id, Department data)
        {
            Department res = DBContext.Departments.FirstOrDefault(x => x.ID == Id);
            try
            {

                res.Title = data.Title;
                res.Director_name = data.Director_name;
                res.Phone_number = data.Phone_number;
                res.Monthly_budget = data.Monthly_budget;
                res.Yearly_budget = data.Yearly_budget;
                res.Website = data.Website;
                res.Amount = data.Amount;
                DBContext.Departments.Update(res);
                DBContext.SaveChanges();
                _cacheClient.RemoveAllCache();
                return res;
            }
            catch
            {
                return null;
            }
        }
    }
}