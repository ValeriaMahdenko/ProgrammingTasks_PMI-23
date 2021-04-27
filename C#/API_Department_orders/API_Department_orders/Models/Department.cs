using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel;
using System.Collections;


namespace API_Department_orders.Models
{
    public class Department
    {

        public int ID { get; set; }

        [RegularExpression(@"^[(a-zA-Z)' '(a-zA-Z)]*$",
            ErrorMessage = "No integers/symbols in string!")]
        public string Title { get; set; }

        [RegularExpression(@"^[(a-zA-Z)' '(a-zA-Z)]*$",
            ErrorMessage = "No integers/symbols in string!")]
        public string Director_name { get; set; }

        [Validation.PhoneCheck]
        public string Phone_number { get; set; }

        [Validation.PriceCheck]
        public double Monthly_budget { get; set; }

        [Validation.PriceCheck]
        public double Yearly_budget { get; set; }

        [Url]
        public string Website { get; set; }

        [Required]
        [Range(0, 10000, ErrorMessage = "Amount must be 0-10000")]
        public int Amount { get; set; }

    }
}