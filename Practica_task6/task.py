from Func_for_task import *
from Context import *
from Observer_classes import *

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
    positions = []
    positions.append(start)
    positions.append(finish)
    return positions


def delete_el(list):
    pos = v.valid_positive("Enter position in list for delete:")
    if pos > len(list):
        print("Position must be < size of list")
    else:
        list.remove(pos)
    return pos


def main():
    list = Double_List()
    context = Context(Strategy_Iterator())
    v = Validate()
    list_of_all_actions = ['Insert data',
                           'Delete element by position(s)']
    Logger.clean_file("Result.txt")

    while True:
        menu()
        response = v.valid_response("Your choice: ")
        if response == 8:
            break

        elif response == 1:
            context = Context(Strategy_Iterator())
        elif response == 2:
            context.strategy = Context(Strategy_File())
        elif response == 3:
            old_list = list.copy()
            position = v.valid_positive("Enter posution:")
            if position > len(list):
                print("Position is wrong!")
            else:
                context.execute(list, position)
            event = Event(list_of_all_actions[0], old_list, list, position, pos2=None)
            Observer.new('Insert data', Logger.write_to_file(event, "Result.txt"))

        elif response == 4:
            old_list = list.copy()
            position = delete_el(list)
            event = Event(list_of_all_actions[1], old_list, list, position, pos2=None)
            Observer.new('Delete element by position(s)', Logger.write_to_file(event, "Result.txt"))


        elif response == 5:
            old_list = list.copy()
            positions = delete_in_range(list)
            event = Event(list_of_all_actions[1], old_list, list, pos1=None, pos2=positions)
            Observer.new('Delete element by position(s)', Logger.write_to_file(event, "Result.txt"))

        elif response == 6:
            pair_gcd(list)
        elif response == 7:
            print(list)
        '''if response == 3 or response == 4 or response == 5:
            Observer.attach('add', Logger.write_to_file(event, "Result.txt"))
            print("Yeeeeeeeeeeeeees")
            print(event)'''

main()