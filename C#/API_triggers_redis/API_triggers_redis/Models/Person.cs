using System;
using System.ComponentModel.DataAnnotations;

namespace API_triggers_redis.Models
{
    public enum Roles
    {
        Admin = 1,
        User = 2
    }
    public class Person
    {
        [Key]
        public int ID { get; set; }

        [Required]
        [EmailAddress]
        public string Email { get; set; }

        [Required]
        public string Password { get; set; }

        [EnumDataType(typeof(Roles))]
        public string Role { get; set; }
    }

    public class LoginData
    {
        public string Email { get; set; }
        public string Password { get; set; }
    }

}
