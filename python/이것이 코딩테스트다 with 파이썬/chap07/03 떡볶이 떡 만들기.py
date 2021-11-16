import math


def binary_search(arr, target, start, end):
    while start <= end:
        sum_len = 0

        mid = (start + end) // 2  # 자름의 길이
        for cake_len in arr:

            # 남은 길이 구하기
            remain = cake_len - mid
            if remain > 0:
                sum_len += remain

        # 결과에 따라 처리하기
        if sum_len == target:
            return mid

        elif sum_len > target:  # 자르는 길이를 더 길게 (더 많이 잘라야됨)
            start = mid + 1

        else:  # 자르는 길이를 더 짧게 (더 조금 잘라야됨)
            end = mid - 1

    return end


# 입력 받기
n, m = map(int, input().split())
cake_list = list(map(int, input().split()))

# 이진탐색 수행하며 (범위: 0 ~ M) 남은 떡의 합이 target이면 stop
result = binary_search(cake_list, m, 0, 1_000_000_000)
print(result)

