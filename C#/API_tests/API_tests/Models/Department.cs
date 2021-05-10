using System;
using System.ComponentModel.DataAnnotations;


namespace API_tests.Models
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

    }
}
