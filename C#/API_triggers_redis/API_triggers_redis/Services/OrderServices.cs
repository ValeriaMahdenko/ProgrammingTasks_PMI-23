using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using API_triggers_redis.Models;
using System.Security.Cryptography;
using API_triggers_redis.Cache;


namespace API_triggers_redis.Services
{
    public interface IOrder
    {
        // for all orders
        public List<Order> GetOrders();
        public Order Get_Order(int id);
        public Order Delete_Order(int id);


        //for my_orders
        public List<Order> Get_my_orders(string email);
        public Order Get_my_order(string email, int id);
        public Order Post_my_order(string email, Order data);
    }

    public class OrderServices : IOrder
    {
        private Context DBContext = new Context();
        private readonly IRedisCache _cacheClient;

        public OrderServices(Context ctx, IRedisCache cacheClient)
        {
            DBContext = ctx;
            _cacheClient = cacheClient;

        }

        public List<Order> GetOrders()
        {
            List<Order> lst_orders = new List<Order>();
            lst_orders = DBContext.Orders.ToList();
            return lst_orders;
        }

        public Order Get_Order(int id)
        {
            Order getbyid = DBContext.Orders.FirstOrDefault(order => order.Id == id);
            if (getbyid == null)
                return null;
            return getbyid;
        }

        public Order Delete_Order(int id)
        {
            Order res = DBContext.Orders.FirstOrDefault(order => order.Id == id);
            if (res != null)
            {
                DBContext.Orders.Remove(res);
                DBContext.SaveChanges();
                return res;
            }
            return null;
            _cacheClient.RemoveAllCache();

        }

        //for my_orders
        public List<Order> Get_my_orders(string email)
        {
            Person a = DBContext.Users.FirstOrDefault(person => person.Email == email);

            var list_of_orders = DBContext.Orders.ToList();
            List<Order> my_orders = new List<Order>();
            foreach (var order in list_of_orders)
            {
                if (order.UserId == a.ID)
                {
                    my_orders.Add(order);
                }

            }
            return my_orders;
        }

        public Order Get_my_order(string email, int id)
        {
            Person a = DBContext.Users.FirstOrDefault(person => person.Email == email);
            Order getbyid = DBContext.Orders.FirstOrDefault(order => order.UserId == a.ID);
            if (getbyid.Id == id)
                return getbyid;
            return null;
        }

        public Order Post_my_order(string email, Order order_data)
        {
            Person a = DBContext.Users.FirstOrDefault(person => person.Email == email);
            Order to_add = new Order()
            {
                Amount = order_data.Amount,
                Date = DateTime.Now,
                UserId = a.ID,
                ProductId = order_data.ProductId
            };
            Department product = DBContext.Departments.FirstOrDefault(x => x.ID == to_add.ProductId);
            try
            {
                if (product.Amount < to_add.Amount)
                    return null;
                product.Amount -= to_add.Amount;
                DBContext.Departments.Update(product);
                DBContext.Orders.Add(to_add);
                DBContext.SaveChanges(); ;
                return to_add;
            }
            catch
            {
                return null;
            }
            _cacheClient.RemoveAllCache();

        }
    }
}