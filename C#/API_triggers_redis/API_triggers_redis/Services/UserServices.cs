using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using API_triggers_redis.Models;
using System.Security.Cryptography;


namespace API_triggers_redis.Services
{
    public interface IUser
    {
        public ClaimsIdentity Identification(string username, string password);
        public Person AddUser(Person data);
    }

    public class UserServices : IUser
    {
        private Context DBContext = new Context();
        public UserServices(Context ctx)
        {
            DBContext = ctx;
        }

        public Person AddUser(Person data)
        {
            data.Role = "user";
            data.Password = HashPassword(data.Password);
            try
            {
                DBContext.Users.Add(data);
                DBContext.SaveChanges();
                return data;
            }
            catch
            {
                return null;
            }
        }

        public ClaimsIdentity Identification(string username, string password)
        {
            var person = DBContext.Users.FirstOrDefault(u => u.Email == username);

            if (person != null)
            {
                string savedPasswordHash = person.Password;
                byte[] hashBytes = Convert.FromBase64String(savedPasswordHash);
                byte[] salt = new byte[16];
                Array.Copy(hashBytes, 0, salt, 0, 16);
                var pbkdf2 = new Rfc2898DeriveBytes(password, salt, 100000);
                byte[] hash = pbkdf2.GetBytes(20);
                for (int i = 0; i < 20; i++)
                    if (hashBytes[i + 16] != hash[i])
                        return null;

                var claims = new List<Claim>
                {
                    new Claim(ClaimsIdentity.DefaultNameClaimType, person.Email),
                    new Claim(ClaimsIdentity.DefaultRoleClaimType, person.Role)
                };
                ClaimsIdentity claimsIdentity =
                new ClaimsIdentity(claims, "Token", ClaimsIdentity.DefaultNameClaimType,
                                    ClaimsIdentity.DefaultRoleClaimType);
                return claimsIdentity;
            }
            return null;
        }

        public static string HashPassword(string password)
        {
            byte[] salt;
            new RNGCryptoServiceProvider().GetBytes(salt = new byte[16]);

            var pbkdf2 = new Rfc2898DeriveBytes(password, salt, 100000);
            byte[] hash = pbkdf2.GetBytes(20);

            byte[] hashBytes = new byte[36];
            Array.Copy(salt, 0, hashBytes, 0, 16);
            Array.Copy(hash, 0, hashBytes, 16, 20);

            string savedPasswordHash = Convert.ToBase64String(hashBytes);
            return savedPasswordHash;
        }
    }
}
