using System.Collections.Generic;
using System.Threading.Tasks;
using API_triggers_redis.Models;

namespace API_triggers_redis.Cache
{
    public interface IRedisCache
    {
        List<Department> GetProducts(string searchString, string sortOrder,
            string sortType, int offset, int limit);

        void SetProducts(string searchString, string sortOrder,
            string sortType, int offset, int limit, List<Department> products);

        void RemoveAllCache();
    }
}
