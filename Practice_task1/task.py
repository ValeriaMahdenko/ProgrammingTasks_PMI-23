def appropriation(arr):
    for j in range(1, len(arr)):
        arr[j] += arr[j - 1]
    return arr


def finding_ways(size):
    # The function for finding ways.
    arr = [1 for i in range(size)]
    for i in range(size - 1):
        narr = [0 for x in range(len(arr) + 1)]
        for j in range(len(arr)):
            narr[j] += arr[j]
            narr[j + 1] += arr[j]
        arr = narr
        appropriation(arr)
    for i in range(size - 1):
        narr = [0 for x in range(len(arr) - 1)]
        for k in range(len(arr) - 1):
            narr[k] += arr[k]
            narr[k] += arr[k + 1]
        arr = narr
        appropriation(arr)
    return arr[-1]


def validate_size():
    try:
        n = int(input("Enter n: "))
        if n < 0:
            print("Number must be positive!")
            exit(0)
    except ValueError:
        print("Number must be an integer!")
        exit(0)
    return n


n = validate_size()
print("Number of ways:  ", finding_ways(n))
