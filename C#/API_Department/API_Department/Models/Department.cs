using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;
using MySqlConnector;

namespace API_Department.Models
{
    public class Department
    {
       
        public int ID { get; set; }

        [RegularExpression(@"^[(a-zA-Z)' '(a-zA-Z)]*$",
            ErrorMessage = "No integers/symbols in string!")]
        public string title  { get; set; }
         
        [RegularExpression(@"^[(a-zA-Z)' '(a-zA-Z)]*$",
            ErrorMessage = "No integers/symbols in string!")]
        public string director_name { get; set; }
        
        [Validation.PhoneCheck]
        public string phone_number { get; set; }

        [Validation.PriceCheck]
        public double monthly_budget { get; set; }
       
        [Validation.PriceCheck]
        public double yearly_budget { get; set; }
        
        [Url]
        public string website { get; set; }
       
        public Department() { }
        internal App_db DB { get; set; }
        internal Department(App_db Db){
            DB = Db;
        }

        private void Parameters(MySqlCommand cmd)
        {
            cmd.Parameters.AddWithValue("@title", title);
            cmd.Parameters.AddWithValue("@director_name", director_name);
            cmd.Parameters.AddWithValue("@phone_number", phone_number);
            cmd.Parameters.AddWithValue("@monthly_budget", monthly_budget);
            cmd.Parameters.AddWithValue("@yearly_budget", yearly_budget);
            cmd.Parameters.AddWithValue("@website", website);
        }

        public async Task InsertAsync()
        {  
            using var cmd = DB.Connection.CreateCommand();
            cmd.CommandText = @"INSERT INTO department_table (_title, _director_name, _phone_number, _monthly_budget, _yearly_budget, _website_url) VALUES (@title, @director_name, @phone_number, @monthly_budget, @yearly_budget, @website);";
            Parameters(cmd);
            await cmd.ExecuteNonQueryAsync();
            ID = (int)cmd.LastInsertedId;
        }

        public async Task UpdateAsync()
        {
            using var cmd = DB.Connection.CreateCommand();
            cmd.CommandText = "UPDATE department_table SET _title = @title, _director_name = @director_name, _phone_number = @phone_number," +
                "_monthly_budget = @monthly_budget, _yearly_budget = @yearly_budget, _website_url = @website WHERE id = @id;";
            Parameters(cmd);
            cmd.Parameters.AddWithValue("@id", ID);
            await cmd.ExecuteNonQueryAsync();
        }
        
        public async Task DeleteAsync()
        {
            using var cmd = DB.Connection.CreateCommand();
            cmd.CommandText = @"DELETE FROM department_table WHERE id = @id;";
            cmd.Parameters.AddWithValue("@id", ID);
            await cmd.ExecuteNonQueryAsync();
        }
    }
}
