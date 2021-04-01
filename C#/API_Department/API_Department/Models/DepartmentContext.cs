using Microsoft.EntityFrameworkCore;


namespace API_Department.Models
{
    public class DepartmentContext : DbContext
    {
        public DepartmentContext(DbContextOptions<DepartmentContext> options)
            : base(options)
        {}

        public DbSet<Department> TodoItems { get; set; }
    }
}
