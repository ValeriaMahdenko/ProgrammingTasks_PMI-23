using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System;
using API_Department_orders.Models;
using API_Department_orders.Services;
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Collections.Generic;



namespace API_Department_orders.Controllers
{
    [Produces("application/json")]
    [ApiController]
    [Authorize]
    public class UserController : ControllerBase
    {

        protected IUser operations;
        public UserController(IUser o)
        {
            operations = o;
        }

        [AllowAnonymous]
        [HttpPost("/login")]
        public IActionResult Token([FromBody] LoginData data)
        {
            var identity = operations.Identification(data.Email, data.Password);
            if (identity == null)
            {
                return NotFound(new { status = 404, message = $"No departments with email {data.Email}" });
            }

            var now = DateTime.UtcNow;
            JwtSecurityToken jwt = new JwtSecurityToken(
                    issuer: Auth.ISSUER,
                    audience: Auth.AUDIENCE,
                    claims: identity.Claims,
                    expires: now.Add(TimeSpan.FromMinutes(Auth.LIFETIME)),
                    signingCredentials: new SigningCredentials(Auth.GetSymmetricSecurityKey(), SecurityAlgorithms.HmacSha256));
            var encodedJwt = new JwtSecurityTokenHandler().WriteToken(jwt);

            var response = new
            {
                access_token = encodedJwt,
                username = identity.Name
            };

            return Ok(new { status = "200", message = response });
        }

        [AllowAnonymous]
        [HttpPost("/register")]
        public IActionResult RegisterUser([FromBody] Person data)
        {
            var res = operations.AddUser(data);
            if (res == null)
                return BadRequest(new { status = "401", message = "Incorect data!" });
            return new OkObjectResult(new Dictionary<string, dynamic> { { "status", 200 }, { "message", "Success!" }, { "Your ID", res.ID } });
        }
    }
}
