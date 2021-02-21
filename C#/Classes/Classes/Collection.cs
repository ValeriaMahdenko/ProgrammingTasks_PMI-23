/*2. Пошук повинен працювати по всіх полях автоматично без введення параметра пошуку, повинен знаходити всі записи по частковому співпадінні.   +
3. Сортування повинно працювати коректно і бути універсальним методом для всіх полів. Значення Test test повинні знаходитись поруч.  -------------------
4. Додати можливість видалення запису (+ запис у файл) по ідентифікатору  +
5. Додати можливість додавання запису (+ запис у файл)   +
6. Додати можливість редагування запису (+ запис у файл) по ідентифікатору   +
*/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.ComponentModel;
using System.IO;
using System.Threading.Tasks;
using System.Text.RegularExpressions;


namespace Classes
{
    class Collection
    {
        private List<Department> _mas = new List<Department>();
        List<Department> mas
        {
            get => _mas;
            set { _mas = value; }
        }

        public int Count()
        {
            return mas.Count();
        }

        public void print()
        {
            for (int i = 0; i < mas.Count(); i++)
                Console.WriteLine(mas[i].print());
        }

        public void read_txt(string path)
        {
            try
            {
                using (StreamReader sr = new StreamReader(path, System.Text.Encoding.Default))
                {
                    int counter = 0;
                    string line;
                    while ((line = sr.ReadLine()) != null)
                    {
                        counter++;
                        try
                        {
                            Department a = new Department();
                            string[] s = line.Split(' ');
                            var type = a.GetType();
                            int i = 0;
                            for (int j = 0; j < s.Count(); j++)
                            {
                                var properties = TypeDescriptor.GetProperties(type);
                                var property = properties[i];
                                if (i >= 4 && i <= 5)
                                    property.SetValue(a, Convert.ToDouble(s[j]));
                                else
                                    property.SetValue(a, s[j]);
                                if (i >= s.Count() - 1)
                                    break;
                                i++;
                            }
                            mas.Add(a);
                        }
                        catch (ArgumentException e)
                        {
                            Console.WriteLine(counter.ToString() + ": " + e.Message);
                        }
                    }
                }
            }
            catch (FileNotFoundException e)
            {
                Console.WriteLine(e.Message);
            }
        }

        public void delete_id(string iden)
        {
            int counter = 0;
            for (int i = 0; i < mas.Count; i++)
            {
                if (mas[i].ID == iden)
                {
                    counter += 1;
                    mas.Remove(mas[i]);
                }
            }
            if (counter > 0)
                Console.WriteLine("Successfully!\n");
            else
                Console.WriteLine("No element in list with ID " + iden);
        }

        public void sort(string key, string desc = null)
        {
            int counter = 0;
            for (int i = 0; i < mas.Count; i++)
            {
                foreach (PropertyDescriptor j in TypeDescriptor.GetProperties(mas[i]))
                    if (j.Name == key)
                        counter++;
            }
            if (counter > 0)
            {

                if (desc != null)
                    mas = mas.OrderByDescending(r => r.GetType().GetProperty(key).GetValue(r, null)).ToList();

                else
                    mas = mas.OrderBy(r => r.GetType().GetProperty(key).GetValue(r, null)).ToList();
                Console.WriteLine("Successfully!\n");
            }
            else
                Console.WriteLine("Sort key is incorrect!");
        }
        public void add()
        {
            try
            {
                Department element = new Department();
                element.input();
                mas.Add(element);
                Console.WriteLine("Successfully!\n");
            }
            catch (ArgumentException e)
            {
                Console.WriteLine(e.Message);
            }
        }

        public void edit_id(string iden)
        {
            int counter = 0;
            for (int i = 0; i < mas.Count; i++)
            {
                if (mas[i].ID == iden)
                {
                    try
                    {
                        counter++;
                        Department element = new Department();
                        element.input();
                        mas.Insert(i, element);
                        mas.Remove(mas[i + 1]);
                        Console.WriteLine("Successfully!\n");
                    }
                    catch (ArgumentException e)
                    {
                        Console.WriteLine(e.Message);
                    }
                }
            }
            if (counter == 0)
                Console.WriteLine("No element in list with ID " + iden);
        }

        public void search(string key)
        {
            foreach (Department obj in mas)
            {
                var type = obj.GetType();
                var properties = TypeDescriptor.GetProperties(type);
                for (int i = 0, n = properties.Count; i < n; i++)
                {
                    var property = properties[i];
                    string el = Convert.ToString(property.GetValue(obj));
                    if (Regex.IsMatch(el.ToLower(), key.ToLower()))
                    {
                        Console.WriteLine(obj.print());
                        break;
                    }
                }
            }
        }

        public void write_txt(string path)
        {
            try
            {
                using (StreamWriter sw = new StreamWriter(path, false, System.Text.Encoding.Default))
                {
                    foreach (Department obj in mas)
                    {
                        var type = obj.GetType();

                        var properties = TypeDescriptor.GetProperties(type);
                        for (int i = 0, n = properties.Count; i < n; i++)
                        {
                            var property = properties[i];
                            sw.Write(property.GetValue(obj));
                            sw.Write(" ");
                        }
                        sw.Write("\n");
                    }
                    Console.WriteLine("Successfully!\n");
                }
            }
            catch (FileNotFoundException e)
            {
                Console.WriteLine(e.Message);
            }
        }
    }

}
