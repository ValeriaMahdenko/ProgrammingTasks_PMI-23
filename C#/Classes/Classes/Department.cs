//Клас ВІДДІЛ: ID, title, director_name, phone_number, monthly_budget, yearly_budget, website_url.
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Classes
{

    class Department
    {
        private string _ID;
        private string _title;
        private string _director_name;
        private string _phone_number;
        private double _monthly_budget;
        private double _yearly_budget;
        private string _website;

        public string ID
        {
            get => _ID;
            set { _ID = Validation.Number(value); }
        }

        public string title
        {
            get => _title;
            set { _title = Validation.String(value); }
        }

        public string director_name
        {
            get => _director_name;
            set { _director_name = Validation.String(value); }
        }

        public string phone_number
        {
            get => _phone_number;
            set { _phone_number = Validation.Phone(value); }
        }

        public double monthly_budget
        {
            get => _monthly_budget;
            set { _monthly_budget = Validation.Price(value); }
        }

        public double yearly_budget
        {
            get => _yearly_budget;
            set
            {
                double el = Validation.Price(Convert.ToDouble(value));
                _yearly_budget = Validation.Price(monthly_budget, el);
            }
        }

        public string website
        {
            get => _website;
            set { _website = Validation.URL(value); }
        }

        public string print()
        {
            return ($"ID: {ID} \nTitle: {title} \nDirector_name: {director_name} \nPhone_number: {phone_number} \nMonthly_budget: {monthly_budget} " +
                $"\nYearly_budget: {yearly_budget} \nWebsite: {website}\n");
        }

        public void input()
        {
            Console.Write("ID: ");
            ID = Console.ReadLine();
            Console.Write("Title: ");
            title = Console.ReadLine();
            Console.Write("Director_name: ");
            director_name = Console.ReadLine();
            Console.Write("Phone_number: ");
            phone_number = Console.ReadLine();
            Console.Write("Monthly_budget: ");
            monthly_budget = int.Parse(Console.ReadLine());
            Console.Write("Yearly_budget: ");
            yearly_budget = int.Parse(Console.ReadLine());
            Console.Write("Website: ");
            website = Console.ReadLine();
        }
    }
}