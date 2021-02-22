using System;
using System.Linq;


namespace Classes
{
    class Validation
    {
        public static string Number(string value)
        {
            int result;
            if (int.TryParse(value, out result))
                return value;
            else
                throw new ArgumentException("No letters/characters in number!");
        }

        public static string String(string value)
        {
            foreach (char c in value)
            {
                if (char.IsDigit(c))
                    throw new ArgumentException("No integers in string!");
            }
            return value;
        }

        public static string Phone(string value)
        {
            if (value.StartsWith("+380") && value.Count() == 13)
                return value;
            else
                throw new ArgumentException("Phone number must be format +380XXXXXXXXX");
        }

        public static double Price(double value)
        {
            decimal d;
            if (!(decimal.TryParse(Convert.ToString(value), out d) && d >= 0 && d * 100 == Math.Floor(d * 100)))
            {
                throw new ArgumentException("Format of budget is wrong!");
            }
            return value;
        }

        public static double Price(double value1, double value2)
        {
            if (value2 <= value1)
                throw new ArgumentException("Mouthly budget must be < than yearly!");
            return value2;
        }

        public static string URL(string value)
        {
            Uri uri = null;
            if (!Uri.TryCreate(value, UriKind.Absolute, out uri) || null == uri)
                throw new ArgumentException("The website_url is not valid");
            else
                return value;
        }
    }
}
