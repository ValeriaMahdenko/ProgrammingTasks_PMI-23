from Department import Department
from Composition import Composition
from Validation import Validation
"""
Створити клас та включити в нього необхідні конструктори та методи доступу до полів класу. 
Перевантажити операції введення, виведення в потік та інші, які необхідні для виконання завдання. 
Вхідні дані зчитувати з текстового файлу.
Створити клас: колекція, який буде працювати з масивом екземплярів класу. 
Програма повинна містити меню для перевірки всіх можливостей.
1. Валідація має бути написана на всі поля, наприклад, не може вік людини бути -10 чи 165. 
При введенні у числове поле літери, необхідно показувати помилку. 
Ім'я чи прізвище не може містити цифри чи спеціальних символів, тощо.
Валідація повинна бути універсальною, тобто окремий метод на перевірку числа, окремий, на те, чи входить в окремі межі.
Валідація - це допоміжні методи, які мають знаходитись в окремому файлі (клас).
2. Пошук повинен працювати по всіх полях автоматично без введення параметра пошуку, повинен знаходити всі записи по 
частковому співпадінні.  
3. Сортування повинно працювати коректно і бути універсальним методом для всіх полів. Значення Test test повинні 
знаходитись поруч.  
4. Додати можливість видалення запису (+ запис у файл) по ідентифікатору  
5. Додати можливість додавання запису (+ запис у файл)  
6. Додати можливість редагування запису (+ запис у файл) по ідентифікатору  
7. Код повинен бути якісним: клас повинен бути в окремому файлі, назва файла не повинна бути захардкоджена, читання з файла - окрема функція, тощо. 
8. Всі методи повинні бути універсальні і не залежати від кількості параметрів класу.   
"""


def menu():
    print("1 - read file")
    print("2 - print list")
    print("3 - add element to list ")
    print("4 - delete element by ID")
    print("5 - sort list")
    print("6 - search")
    print("7 - edit element by ID")
    print("8 - write file")
    print("0 - EXIT")


def validate(message, choice=" "):
    while True:
        try:
            el = int(input(message))
            if choice == "for_response":
                if el < 0 or el >= 9:
                    print("The value is incorrect! Please, try again")
                    continue
            break
        except ValueError:
            print("Number must be an integer! Please, try again")
            continue
    return el

el = Validation()
mas = Composition()
filename = "Information"
while True:
    menu()
    response = validate("Your choice: ", choice="for_response")
    if response == 0:
        print("Thank you for attention!")
        break
    if response == 1:
        if el.validate_file(filename) == True:
            mas.read_txt(filename)
    if response == 2:
        print("\n\n")
        for i in mas: print(i)
    if response == 3:
        print("~~~~~~~~~~~~~~~~ADD~~~~~~~~~~~~~~~~~~~~")
        mas.add_element()
    if response == 4:
        print("~~~~~~~~~~~~~~~~~~~~~~DELETE BY ID~~~~~~~~~~~~~~~~")
        delete = input("ID FOR DELETE:")
        mas.delete_by_id(delete)
    if response == 5:
        print("~~~~~~~~~~~~~Sort~~~~~~~~~~~~~~~~~~")
        word = input("Enter key")
        SORT = mas.sort(key=word)
        for i in SORT: print(i)
    if response == 6:
        print("~~~~~~~~~~~~~~~~~~~~~Search~~~~~~~~~~~~~~~~~~~~~")
        key = input("Enter key:")
        arr = mas.search(key)
        for i in arr: print(i)
    if response == 7:
        print("~~~~~~~~~~~~~~~~~~~~~~EDIT~~~~~~~~~~~~~~~~~~~~")
        edit = input("Id for edit:")
        mas.edit_by_id(edit)
    if response == 8:
        if el.validate_file(filename) == True:
            mas.write_txt(filename)
      
