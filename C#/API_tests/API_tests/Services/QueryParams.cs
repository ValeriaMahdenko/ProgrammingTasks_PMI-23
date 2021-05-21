using System;
using System.Collections.Generic;
using System.Linq;
using API_tests.Models;

namespace API_tests.Services
{
    public class QueryParams
    {
        public List<Department> Search(List<Department> l, string s)
        {
            bool added = false;
            List<Department> res = new List<Department>();
            foreach (var order in l)
            {
                foreach (var prop in order.GetType().GetProperties())
                {
                    if (prop.GetValue(order).ToString().ToLower().Contains(s.ToLower()) && !added)
                    {
                        res.Add(order);
                        added = true;
                    }
                }
                added = false;
            }
            return res;
        }

        public List<Department> Sort(List<Department> l, string sort_type, string sort_by)
        {
            int count = 0;
            foreach (var prop in typeof(Department).GetProperties())
            {
                if (prop.Name == sort_by && sort_type == "desc")
                {
                    l = l.OrderByDescending(c => c.GetType().GetProperty(sort_by).GetValue(c, null)).ToList();
                    return l;
                }
                if (prop.Name == sort_by)
                {
                    l = l.OrderBy(c => c.GetType().GetProperty(sort_by).GetValue(c, null)).ToList();
                    return l;
                }
            }
            return l;
        }

        public List<Department> Paginate(List<Department> l, int page_num, int page_size)
        {
            List<Department> res = l.Skip((page_num - 1) * page_size).Take(page_size).ToList();
            return res;
        }

    }
}
