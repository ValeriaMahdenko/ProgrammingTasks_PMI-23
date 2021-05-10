using System.Collections.Generic;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using API_tests.Models;
using API_tests.Services;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace API_tests.Controllers
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

        /// <summary>
        /// Get all Departments | Search | Sort | Offset | Limit on one page
        /// </summary>
        /// <param name="s"> Function will only return departments that contain "search" substring in any attribute</param>
        /// <param name="sort_by" example="ID">Function will return departments sorted by given attribute</param>
        /// <param name="sort_type" example="asc">Function will return departments in given order</param>
        /// <param name="offset" example="1">Which page we choose?</param>
        /// <param name="limit" example="10">How much departments on one page</param>
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
            Console.WriteLine(res.count);
            if (res.count == 0)
                return BadRequest(new { status = 404, message = "No departments in list" });

            return new OkObjectResult(new Dictionary<string, dynamic> { { "Count", res.count }, { "Objects: ", res.res } });
        }
        /// <summary>
        /// Returns a specific Department by given id
        /// </summary>
        /// <param name="id">Id of Department to get</param>
        [HttpGet("{id}")]
        public ActionResult Get_amount(int id)
        {
            Department res = operations.GetDepartment(id);
            if (res == null)
                return NotFound(new { status = 404, message = $"No departments with id {id}" });

            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" }, { "Object", res } });
        }

        /// <summary>
        /// Creates a new Department.
        /// </summary>
        /// <remarks>
        /// Sample request:
        ///
        /// 
        ///     POST /Department
        ///     {
        ///     "title": "YourTitle",
        ///     "director_name": "YourName",
        ///     "phone_number": "+380500000000",
        ///     "monthly_budget": 1000,
        ///     "yearly_budget": 12000,
        ///     "website":    
        ///     }
        /// </remarks>
        /// <param name="data"></param>
        /// <returns>A newly created Department</returns>
        /// <response code="200">Returns the newly created Department</response>
        /// <response code="400">If Department does not pass validation</response>
        [HttpPost]
        public ActionResult AddProduct([FromBody] Department data)
        {
            Department res = operations.AddDepartment(data);
            if (res == null)
                return BadRequest(new { status = 400, message = $"Incorect data" });
            return Ok(new { status = 200, message = "Successfully!" });
        }

        /// <summary>
        /// Deletes Department by given id
        /// </summary>
        /// <param name="id">ID of Department to delete</param>
        /// <returns>Success Message</returns>
        /// <response code="404">If Departments with ID does not exist</response>  
        [HttpDelete("{id}")]
        public ActionResult DeleteProduct(int id)
        {
            var res = operations.DeleteDepartment(id);
            if (res == null)
                return NotFound(new { status = 400, message = $"No departments with id {id}" });
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" } });
        }

        /// <summary>
        /// Updates Department  by given id
        /// </summary>
        /// <param name="id">Id of Department to update</param>
        /// <param name="data">New Department data</param> 
        /// <remarks>
        /// Sample request:
        ///
        ///     Put /1
        ///     {
        ///     "title": "YourTitle",
        ///     "director_name": "YourName",
        ///     "phone_number": "+380500000000",
        ///     "monthly_budget": 1000,
        ///     "yearly_budget": 12000,
        ///     "website": "https://YourWebsite.com"
        ///     }
        ///
        /// </remarks>
        /// <response code="200"> Updated department </response>
        /// <response code="400"> Department is null / Department does not pass validation / Id is of wrong type </response>  
        /// <response code="404"> Department with this id was not found </response>  
        [HttpPut("{id}")]
        public ActionResult Put_Department(int id, Department data)
        {
            var res = operations.PutDepartment(id, data);
            if (res == null)
                return NotFound(new { status = 404, message = $"No departments with id {id}" });
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" }, { "Object", res } });
        }
    }
}
