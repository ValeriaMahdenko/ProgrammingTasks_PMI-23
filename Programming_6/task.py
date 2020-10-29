from Department import Department
from Composition import Composition
from Validation import Validation
from Memento import *
def menu():
    print("1 - read file")
    print("2 - print list")
    print("3 - add element to list ")
    print("4 - delete element by ID")
    print("5 - sort list")
    print("6 - search")
    print("7 - edit element by ID")
    print("8 - write file")
    print("prev  - command undo ")
    print("next - command redo")
    print("0 - EXIT")


def printState(originator):
    for i in originator.getNote():
        print(i)

def add_Memento(originator, caretaker, mas):
    originator.setNote(mas)
    caretaker.addMemento(originator.save())


def main():
    mas = Composition()
    filename = "Information"
    originator = Originator()
    caretaker = CareTaker()
    add_Memento(originator, caretaker, mas)
    while True:
        menu()
        response = input("Your choice: ")
        if response == "0":
            print("Thank you for attention!")
            break
        elif response == "1":
            mas.read_txt(filename)
            add_Memento(originator, caretaker, mas)

        elif response == "2":
            print("\n")
            for i in mas: print(i)

        elif response == "3":
            print("~~~~~~~~~~~~~~~~ADD~~~~~~~~~~~~~~~~~~~~")
            mas.add_element()
            add_Memento(originator, caretaker, mas)

        elif response == "4":
            print("~~~~~~~~~~~~~~~~~~~~~~DELETE BY ID~~~~~~~~~~~~~~~~")
            delete = input("ID FOR DELETE:")
            mas.delete_by_id(delete)
            add_Memento(originator, caretaker, mas)

        elif response == "5":
            print("~~~~~~~~~~~~~Sort~~~~~~~~~~~~~~~~~~")
            word = input("Enter key")
            mas.sort(key=word)
            add_Memento(originator, caretaker, mas)

        elif response == "6":
            print("~~~~~~~~~~~~~~~~~~~~~Search~~~~~~~~~~~~~~~~~~~~~")
            key = input("Enter key: ")
            search = mas.search(key)
            for i in search: print(i)

        elif response == "7":
            print("~~~~~~~~~~~~~~~~~~~~~~EDIT~~~~~~~~~~~~~~~~~~~~")
            edit = input("Id for edit:")
            mas.edit_by_id(edit)
            add_Memento(originator, caretaker, mas)

        elif response == "8":
            mas.write_txt(filename)

        elif response == "prev":
            originator.restore(caretaker.undo())
            printState(originator)

        elif response == "next":
            originator.restore(caretaker.redo())
            printState(originator)

        else:
            print("The value is incorrect! Please, try again")


main()
