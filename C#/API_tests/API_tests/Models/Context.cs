using Microsoft.EntityFrameworkCore;


namespace API_tests.Models
{
    public class Context : DbContext
    {
        public Context() { }

        public Context(DbContextOptions<Context> options) : base(options) { }

        public DbSet<Department> Departments { get; set; }
    }
}
