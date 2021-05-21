using System;
using System.Linq;
using System.ComponentModel.DataAnnotations;

namespace API_triggers_redis.Models
{
    public static class Validation
    {
        public class PhoneCheck : ValidationAttribute
        {
            public override bool IsValid(object value)
            {
                string v = value as string;
                if (v.StartsWith("+380") && v.Count() == 13)
                    return true;
                else
                {
                    ErrorMessage = "Phone number must be format +380XXXXXXXXX";
                    return false;
                }
            }
        }

        public class PriceCheck : ValidationAttribute
        {
            public override bool IsValid(object value)
            {
                decimal d;
                if (!(decimal.TryParse(Convert.ToString(value), out d) && d >= 0 && d * 100 == Math.Floor(d * 100)))
                {
                    ErrorMessage = "Format of budget is wrong!";
                    return false;
                }
                return true;
            }
        }

    }
}
