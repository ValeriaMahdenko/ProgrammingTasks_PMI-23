using System.Collections.Generic;
using System.Threading.Tasks;
using Newtonsoft.Json;
using API_triggers_redis.Models;
using StackExchange.Redis;

namespace API_triggers_redis.Cache
{
    public class RedisCache : IRedisCache
    {
        private readonly IConnectionMultiplexer _connectionMultiplexer;
        private readonly IDatabase _database;

        public RedisCache(IConnectionMultiplexer connectionMultiplexer)
        {
            _connectionMultiplexer = connectionMultiplexer;
            _database = connectionMultiplexer.GetDatabase();
        }

        public List<Department> GetProducts(string searchString, string sortOrder,
            string sortType, int offset, int limit)
        {
            var searchKey = SetKey(searchString, sortOrder, sortType, offset, limit);
            string searchCache = _database.StringGet(searchKey);
            return searchCache is null ? null : JsonConvert.DeserializeObject<List<Department>>(searchCache);
        }

        public void SetProducts(string searchString, string sortOrder,
            string sortType, int offset, int limit, List<Department> products)
        {
            var searchKey = SetKey(searchString, sortOrder, sortType, offset, limit);
            var strProducts = JsonConvert.SerializeObject(products);
            _database.StringSet(searchKey, strProducts);
        }

        public void RemoveAllCache()
        {
            var endpoints = _connectionMultiplexer.GetEndPoints(true);
            foreach (var endpoint in endpoints)
            {
                var server = _connectionMultiplexer.GetServer(endpoint);
                server.FlushAllDatabases();
            }
        }

        private string SetKey(string searchString, string sortOrder,
            string sortType, int offset, int limit) => $"Search - {searchString}, Sort by - {sortOrder}, Sort type - {sortType}," +
            $"Offset - {offset}, Limit - {limit}";

    }
}
