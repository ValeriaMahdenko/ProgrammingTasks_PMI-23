def menu():
    print("1 - New matrix!")
    print("0 - EXIT")


def validate(message, choice=" "):
    while True:
        try:
            el = int(input(message))
            if choice == "no_neg":
                if el <= 0:
                    print("Number must be positive! Please, try again")
                    continue
            if choice == "for_response":
                if el < 0 or el >= 2:
                    print("The value is incorrect! Please, try again")
                    continue
            break
        except ValueError:
            print("Number must be an integer! Please, try again")
            continue
    return el


def print_matrix(matr, n, message):
    print(message)
    for i in range(n):
        for j in range(len(matr[i])):
            print(matr[i][j], end=' ')
        print()


def create_diagonal(matr, n):
    el = n
    for i in range(n):
        matr[i][i] = i+1
        matr[i][n-1-i] = el
        el -= 1


while True:
    menu()
    response = validate("Your choice: ", choice="for_response")
    if response == 0:
        print("Thank you for attention!")
        break
    if response == 1:
        size = validate("Enter n: ", choice="no_neg")
        matrix = [[0] * size for i in range(size)]
        create_diagonal(matrix, size)
        print_matrix(matrix, size, "Our result sequence: ")