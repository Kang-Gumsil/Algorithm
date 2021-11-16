def print_arr(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
    print()


def print_arr_1(arr):
    for i in arr[1:]:
        for j in i[1:]:
            print(j, end=" ")
        print()
    print()