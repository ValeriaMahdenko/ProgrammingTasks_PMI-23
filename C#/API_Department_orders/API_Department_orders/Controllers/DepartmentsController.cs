using System.Collections.Generic;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using API_Department_orders.Models;
using API_Department_orders.Services;
using API_Department_orders.Response;

namespace API_Department_orders.Controllers
{
    [Produces("application/json")]
    [Route("departments/")]
    [ApiController]
    public class DepartmentsController : ControllerBase
    {
        protected IDepartment operations;
        public DepartmentsController(IDepartment o)
        {
            operations = o;
        }

        [HttpGet]
        public ActionResult Get_all_departments(string s, string sort_by, string sort_type, int offset, int limit)
        {
            Parameters a = new Parameters
            {
                Search = s,
                Sort_by = sort_by,
                Sort_type = sort_type,
                Limit = limit,
                Offset = offset
            };
            var res = operations.GetDepartments(a);
            if (res.count == 0)
                return BadRequest(new { status = 404, message = "No departments in list" });

            return new OkObjectResult(new Dictionary<string, dynamic> { { "Count", res.count }, { "Objects: ", res.res } });
        }
        [HttpGet("{id}")]
        public ActionResult Get_amount(int Id)
        {
            Department res = operations.GetDepartment(Id);
            if (res == null)
                return NotFound(new { status = 404, message = $"No departments with id {Id}" });

            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" }, { "Object", res } });
        }

        [HttpPost]
        [Authorize(Roles = "admin")]
        public ActionResult AddProduct([FromBody] Department data)
        {
            Department res = operations.AddDepartment(data);
            if (res == null)
                return BadRequest(new { status = 400, message = $"Incorect data" });
            return Ok(new { status = 200, message = "Successfully!" });
        }

        [HttpDelete("{id}")]
        [Authorize(Roles = "admin")]
        public ActionResult DeleteProduct(int id)
        {
            var res = operations.DeleteDepartment(id);
            if (res == null)
                return BadRequest(new { status = 400, message = $"No departments with id {id}" });
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" } });
        }


        [HttpPut("{id}")]
        [Authorize(Roles = "admin")]
        public ActionResult Put_Department(int Id, Department data)
        {
            var res = operations.PutDepartment(Id, data);
            if (res == null)
                return NotFound(new { status = 404, message = $"No departments with id {Id}" });
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" }, { "Object", res } });
        }
    }
}
