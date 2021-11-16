def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


answer = ""
n = int(input())
stock_list = list(map(int, input().split()))

m = int(input())
order_list = list(map(int, input().split()))

stock_list.sort()
for order in order_list:
    if binary_search(stock_list, order, 0, n - 1) is not None:
        answer += "yes "
    else:
        answer += "no "

print(answer)
