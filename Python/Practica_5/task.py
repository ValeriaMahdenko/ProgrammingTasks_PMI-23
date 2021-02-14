from Func_for_task import *
from Context import *

def menu():
    print("1 - Strategy 1")
    print("2 - Strategy 2")
    print("3 - Generate")
    print("4 - Delete element")
    print("5 - Delete in range")
    print("6 - Metod in task")
    print("7 - Print list")
    print("8 - EXIT")


def delete_in_range(list):
    start = v.valid_positive("Enter position for start: ")
    finish = v.valid_positive("Enter position for finish: ")
    if start > finish:
        print("Start_position must be < finish_position")
    elif finish > len(list):
        print("Finish must be < size of list")
    else:
        count = finish - start + 1
        for i in range(count):
            list.remove(start)


def delete_el(list):
    pos = v.valid_positive("Enter position in list for delete:")
    if pos > len(list):
        print("Position must be < size of list")
    else:
        list.remove(pos)


def main():
    list = Double_List()
    context = Context(Strategy_1())
    v = Validate()
    while True:
        menu()
        response = v.valid_response("Your choice: ")
        if response == 8:
            break
        if response == 1:
            context = Context(Strategy_1())
        if response == 2:
            context.strategy = Context(Strategy_2())
        if response == 3:
            position = v.valid_positive("Enter posution:")
            if position > len(list):
                print("Position is wrong!")
            else:
                context.execute(list, position)
        if response == 4:
            delete_el(list)
        if response == 5:
            delete_in_range(list)
        if response == 6:
            pair_gcd(list)
        if response == 7:
            print(list)


main()