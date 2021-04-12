using Microsoft.EntityFrameworkCore;
namespace API_Department_orders.Models
{
    public class Context :DbContext
    {
        public Context() { }
       
        public Context(DbContextOptions<Context> options) : base(options) { }
         
        public DbSet<Order> Orders { get; set; }
        public DbSet<Person> Users { get; set; }
        public DbSet<Department> Departments { get; set; }
    }
}
