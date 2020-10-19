from Department import Department
from Composition import Composition
from Validation import Validation
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

def main():
    mas = Composition()
    el = Validation()
    filename = "Information"
    while True:
        menu()
        response = input("Your choice: ")
        if response == "0":
            print("Thank you for attention!")
            break
        if response == "1":
            mas.read_txt(filename)
        if response == "2":
            print("\n")
            for i in mas: print(i)
        if response == "3":
            print("~~~~~~~~~~~~~~~~ADD~~~~~~~~~~~~~~~~~~~~")
            mas.add_element()
        if response == "4":
            print("~~~~~~~~~~~~~~~~~~~~~~DELETE BY ID~~~~~~~~~~~~~~~~")
            delete = input("ID FOR DELETE:")
            mas.delete_by_id(delete)
        if response == "5":
            print("~~~~~~~~~~~~~Sort~~~~~~~~~~~~~~~~~~")
            word = input("Enter key")
            SORT = mas.sort(key=word)
            for i in SORT: print(i)
        if response == "6":
            print("~~~~~~~~~~~~~~~~~~~~~Search~~~~~~~~~~~~~~~~~~~~~")
            key = input("Enter key:")
            arr = mas.search(key)
            for i in arr: print(i)
        if response == "7":
            print("~~~~~~~~~~~~~~~~~~~~~~EDIT~~~~~~~~~~~~~~~~~~~~")
            edit = input("Id for edit:")
            mas.edit_by_id(edit)
        if response == "8":
            mas.write_txt(filename)
        else:
            print("The value is incorrect! Please, try again")

main()
