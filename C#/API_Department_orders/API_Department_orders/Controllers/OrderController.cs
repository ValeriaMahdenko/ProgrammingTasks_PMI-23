using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using API_Department_orders.Models;
using API_Department_orders.Services;
using Microsoft.AspNet.Identity;


namespace API_Department_orders.Controllers
{
    [Produces("application/json")]
    [ApiController]
    public class OrderController: ControllerBase
    {

        protected IOrder operations;
        public OrderController(IOrder o)
        {
            operations = o;
        }

        [HttpGet]
        [Route("myorders/")]
        [Authorize(Roles = "user")]
        public ActionResult Get_my_orders()
        {
            var res = operations.Get_my_orders(User.Identity.GetUserName());
            if (res is null)
                return NotFound();
            return new OkObjectResult(new Dictionary<string, dynamic> { { "Count", res.Count }, { "Objects: ", res } });
        }

        [HttpGet]
        [Route("myorders/{id}")]
        [Authorize(Roles = "user")]
        public ActionResult Get_my_one_order(int id)
        {
            var res = operations.Get_my_order(User.Identity.GetUserName(), id);
            if (res is null)
                return BadRequest(new { status = 404, message = $"No orders in list with id {id}" });
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" }, { "Object", res } });
        }

        [HttpPost]
        [Route("myorders/")]
        [Authorize(Roles = "user")]
        public ActionResult Create_my_order([FromBody] Order orderData)
        {
            var res = operations.Post_my_order(User.Identity.GetUserName(), orderData);
            if (res is null)
                return BadRequest(new { status = 400, message = $"Incorect data" });
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" }, { "Your order", res } });
        }

        [HttpGet]
        [Route("orders/")]
        [Authorize(Roles = "admin")]
        public ActionResult Get_orders()
        {
            var res = operations.GetOrders();
            return new OkObjectResult(new Dictionary<string, dynamic> { { "Count", res.Count}, { "Objects: ", res } });
        }

        [HttpGet]
        [Route("orders/{id}")]
        [Authorize(Roles = "admin")]
        public ActionResult Get_order(int id)
        {
            var res = operations.Get_Order(id);
            if (res is null)
                return BadRequest(new { status = 404, message = $"No orders in list with id {id}" });
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" }, { "Object", res } });
        }

        [HttpDelete("orders/{id}")]
        [Authorize(Roles = "admin")]
        public ActionResult Delete_Order(int id)
        {
            var res = operations.Delete_Order(id);
            if (res == null)
                return BadRequest(new { status = 400, message = $"No departments with id {id}" });
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" } });
        }
    }
}