using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using API_Department.Models;

namespace API_Department.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class DepartmentsController : ControllerBase
    {
        public App_db Db { get; }
        public DepartmentsController(App_db db)
        {
            Db = db;
        }

        // GET: api/Departments
        [HttpGet]
        public async Task<IActionResult> GetLatest([FromQuery ] Parameters parameters)
        {
            await Db.Connection.OpenAsync();
            var query = new DepartmentQuery(Db);
            var all = await query.all_Async();
            var result = await query.AllAsync(parameters);
            return new OkObjectResult(new Dictionary<string, dynamic> { { "Count", all.Count }, { "Objects: ", result } });
        }

        // GET: api/Departments/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Department>> GetDepartment(int id)
        {
            await Db.Connection.OpenAsync();
            var query = new DepartmentQuery(Db);
            var result = await query.FindOneAsync(id);
            if (result is null)
                return new NotFoundResult();
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" }, { "Object", result } });
        }

        // PUT: api/Departments/5
        [HttpPut("{id}")]
        public async Task<IActionResult> PutDepartment(int id, Department department)
        {
            await Db.Connection.OpenAsync();
            var query = new DepartmentQuery(Db);
            var result = await query.FindOneAsync(id);
            if (result is null)
                return new NotFoundResult();
            result.title = department.title;
            result.director_name = department.director_name;
            result.phone_number = department.phone_number;
            result.monthly_budget = department.monthly_budget;
            result.yearly_budget = department.yearly_budget;
            result.website = department.website;
            await result.UpdateAsync();
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" }, { "Object", result } });
        }

        // POST: api/Departments
        [HttpPost]
        public async Task<ActionResult<Department>> PostDepartment(Department department)
        {
            await Db.Connection.OpenAsync();
            department.DB = Db;
            await department.InsertAsync();
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" }, { "Object", department } });
        }

        // DELETE: api/Departments/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteDepartment(int id)
        {
            await Db.Connection.OpenAsync();
            var query = new DepartmentQuery(Db);
            var result = await query.FindOneAsync(id);
            if (result is null)
                return new NotFoundResult();
            await result.DeleteAsync();
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" } } );
        }

    }
}
