using System.Collections.Generic;
using System.Data.Common;
using System.Threading.Tasks;
using System;

namespace API_Department.Models
{
    public class DepartmentQuery
    {
        public App_db Db { get; }

        public DepartmentQuery(App_db db)
        {
            Db = db;
        }
        public async Task<Department> FindOneAsync(int id)
        {
            using var cmd = Db.Connection.CreateCommand();
            cmd.CommandText = @"SELECT * FROM department_table WHERE `id` = @id";
            cmd.Parameters.AddWithValue("@id", id);
            var result = await ReadAllAsync(await cmd.ExecuteReaderAsync());
            if (result.Count > 0)
                    return result[0];
            else return null;
        }
        public async Task<List<Department>> All_Async()
        {
            using var cmd = Db.Connection.CreateCommand();
            cmd.CommandText = @"SELECT * FROM department_table";
            return await ReadAllAsync(await cmd.ExecuteReaderAsync());
        }

        public async Task<List<Department>> AllAsync( Parameters param)
        {
            using var cmd = Db.Connection.CreateCommand();
            cmd.CommandText = @"SELECT * FROM department_table";
            if (param.Search != null)
                cmd.CommandText = cmd.CommandText +
                    " WHERE _title LIKE '%" + param.Search + "%' OR _director_name LIKE '%" + param.Search + "%' OR _phone_number LIKE '%" + param.Search + 
                    "%' OR _monthly_budget LIKE '%" + param.Search + "%' OR _yearly_budget LIKE '%" + param.Search + "%' OR _website_url LIKE '%" + param.Search + "%'";
            if (param.Sort_by != null && param.Sort_type == "asc" || param.Sort_by != null && param.Sort_type == "desc")
                cmd.CommandText += " ORDER BY " + "_"+param.Sort_by + " " + param.Sort_type;
            if (param.Limit != 0)
                cmd.CommandText += " LIMIT " + param.Limit;
            if (param.Offset > 0)
                cmd.CommandText += " OFFSET " + (param.Offset-1)*param.Limit;

            System.Diagnostics.Debug.WriteLine(cmd.CommandText);
            return await ReadAllAsync(await cmd.ExecuteReaderAsync());
        }

        public async Task<List<Department>> all_Async()
        {
            using var cmd = Db.Connection.CreateCommand();
            cmd.CommandText = @"SELECT * FROM department_table";
            return await ReadAllAsync(await cmd.ExecuteReaderAsync());
        }

        private async Task<List<Department>> ReadAllAsync(DbDataReader reader)
        {
            var all = new List<Department>();
            using (reader)
            {
                while (await reader.ReadAsync()) 
                {
                    var post = new Department(Db)
                    {
                        ID = Convert.ToInt32(reader[0]),
                        title = reader[1].ToString(),
                        director_name = reader[2].ToString(),
                        phone_number = reader[3].ToString(),
                        monthly_budget = Convert.ToDouble(reader[4]),
                        yearly_budget = Convert.ToDouble(reader[5]),
                        website = reader[6].ToString()
                    };
                    all.Add(post);
                }
            }
            return all;
        }
    }

}