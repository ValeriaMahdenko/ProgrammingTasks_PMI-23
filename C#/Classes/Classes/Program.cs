using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Classes
{
    class Program
    {
        static void menu()
        {
            Console.WriteLine("1 - read file \n2 - print list \n3 - add element to list \n4 - delete element by ID \n5 - sort list \n6 - search \n7 - edit element by ID " +
                "\n8 - write file \n0 - EXIT");
        }

        static void MainMenu()
        {
            Collection b = new Collection();
            while (true)
            {
                menu();
                Console.Write("\r\nSelect an option: ");
                string response = Console.ReadLine();
                if (response == "1")
                {
                    Console.Write("Enter the path of file: ");
                    string path = Console.ReadLine();
                    b.read_txt(path);
                }
                else if (response == "2")
                {
                    Console.WriteLine("\tYour list: ");
                    b.print();
                }
                else if (response == "3")
                {
                    Console.WriteLine("~~~~~~~~~~~~~~~~~~~~~~ADD~~~~~~~~~~~~~~~~~~~~");
                    b.add();
                }
                else if (response == "4")
                {
                    Console.WriteLine("~~~~~~~~~~~~~~~~~~~~~~DELETE BY ID~~~~~~~~~~~~~~~~~~~");
                    Console.Write("ID FOR DELETE: ");
                    try
                    {
                        string el = Validation.Number(Console.ReadLine());
                        b.delete_id(el);
                    }
                    catch (ArgumentException e)
                    {
                        Console.WriteLine(e.Message);
                    }
                }
                else if (response == "5")
                {
                    Console.WriteLine("~~~~~~~~~~~~~~~~~~~~~~~~~SORT~~~~~~~~~~~~~~~~~~~~~~~~");
                    Console.Write("Enter key: ");
                    string word = Console.ReadLine();
                    Console.Write("Desc or asc: ");
                    string choice = Console.ReadLine();
                    if (choice == "desc")
                        b.sort(word, choice);
                    else
                        b.sort(word);
                }
                else if (response == "6")
                {
                    Console.WriteLine("~~~~~~~~~~~~~~~~~~~~~~~~~SEARCH~~~~~~~~~~~~~~~~~~~~~~~~");
                    Console.Write("Enter key: ");
                    string word = Console.ReadLine();
                    b.search(word);

                }
                else if (response == "7")
                {
                    Console.WriteLine("~~~~~~~~~~~~~~~~~~~~~~~~~EDIT BY ID~~~~~~~~~~~~~~~~~~~~~~~~");
                    try
                    {
                        Console.Write("ID for edit: ");
                        string word = Validation.Number(Console.ReadLine());
                        b.edit_id(word);
                    }
                    catch (ArgumentException e)
                    {
                        Console.WriteLine(e.Message);
                    }
                }
                else if (response == "8")
                {
                    Console.Write("Enter the path of file: ");
                    string path = Console.ReadLine();
                    b.write_txt(path);
                }
                else if (response == "0")
                {
                    Console.WriteLine("Thank you for attention!");
                    break;
                }
                else
                {
                    Console.WriteLine("The value is incorrect! Please, try again");
                    continue;
                }
            }
        }


        static void Main(string[] args)
        {
            Console.WriteLine("\t\tHello! \n");
            MainMenu();
            Console.WriteLine("\t\tGoodbye! Have a nice day!");
        }
    }
}
