from Func_for_task import *
from Context import *
import threading
from Observer_classes import *
import time

def menu():
    print("1 - Strategy 1")
    print("2 - Strategy 2")
    print("3 - Generate")
    print("4 - Delete element")
    print("5 - Delete in range")
    print("6 - Metod in task")
    print("7 - Print list")
    print("8 - EXIT")

def delete_range(lst, finish, start):
    count = finish - start + 1
    for i in range(count):
        lst.remove(start)
    return lst

def delete_in_range(list_iter, list_file):
    counter = 0
    copy_iter = list_iter.copy()
    cope_file = list_file.copy()
    start = v.valid_positive("Enter position for start: ")
    finish = v.valid_positive("Enter position for finish: ")
    if start > finish:
        counter+=1
        print("Start_position must be < finish_position")
    if finish < len(list_iter):
        th1 = create_thread(delete_range, list_iter,  finish, start)
    if finish < len(list_file):
        th2 = create_thread(delete_range, list_file,  finish, start)
    else:
        counter+=1
        print("Finish must be < size of list")
    if counter == 0:
        process([th1, th2])

    event = Event('Delete element by position(s)', copy_iter, list_iter, pos1=None, pos2=[start, finish])
    Observer.new('Delete element by position(s)', Logger.write_to_file(event, "Result.txt"))
    event = Event('Delete element by position(s)', cope_file, list_file, pos1=None, pos2=[start, finish])
    Observer.new('Delete element by position(s)', Logger.write_to_file(event, "Result.txt"))


def delete_el(list_iter, list_file):
    counter = 0
    copy_iter = list_iter.copy()
    cope_file = list_file.copy()
    pos = v.valid_positive("Enter position in list for delete:")
    if pos < len(list_iter):
        th1 = create_thread(list_iter.remove, pos)
    if pos < len(list_file):
        th2 = create_thread(list_file.remove, pos)
    else:
        counter+=1
        print("Position must be < size of list ")
    if counter == 0:
        process([th1, th2])

    event = Event('Delete element by position(s)', copy_iter, list_iter, pos, pos2=None)
    Observer.new('Delete element by position(s)', Logger.write_to_file(event, "Result.txt"))
    event = Event('Delete element by position(s)', cope_file, list_file, pos, pos2=None)
    Observer.new('Delete element by position(s)', Logger.write_to_file(event, "Result.txt"))


def process(list):
    for i in list:
        print("starting...")
        i.start()
        print("finishing...")
        i.join()


def print_list(list):
    for i in range(len(list)):
        print(list[i], end=" ")
    print("\n")


def create_thread(func, *arg):
    thread_1 = threading.Thread(target=func, args=[*arg, ])
    return thread_1

def main():
    list_iter = Double_List()
    list_file = Double_List()
    context = Context(Strategy_Iterator())
    v = Validate()
    list_of_all_actions = ['Insert data',
                           'Delete element by position(s)']
    Logger.clean_file("Result.txt")
    while True:
        menu()
        response = v.valid_response("Your choice: ")
        old_iter = list_iter.copy()
        old_file = list_file.copy()
        if response == 8:
            break
        if response == 1:
            context = Context(Strategy_Iterator())
            response_ = 1
        if response == 2:
            context.strategy = Context(Strategy_File())
            response_ = 2
        if response == 3:
            position = v.valid_positive("Enter posution:")
            if position <= len(list_iter) and response_ == 1:
                context.execute(list_iter, position)
                event = Event(list_of_all_actions[0], old_iter, list_iter, position, pos2=None)
                Observer.new('Insert data', Logger.write_to_file(event, "Result.txt"))
            elif position <= len(list_file) and response_ == 2:
                context.execute(list_file, position)
                event = Event(list_of_all_actions[0], old_file, list_file, position, pos2=None)
                Observer.new('Insert data', Logger.write_to_file(event, "Result.txt"))
            else:
                print("Position is wrong!")
        if response == 4:
           delete_el(list_iter, list_file)
        if response == 5:
            delete_in_range(list_iter, list_file)
        if response == 6:
            th1 = create_thread(pair_gcd, [*list_iter])
            th2 = create_thread(pair_gcd, [*list_file])
            process([th1, th2])
        if response == 7:
            th1 = create_thread(print_list, list_iter)
            th2 = create_thread(print_list, list_file)
            process([th1, th2])

main()
