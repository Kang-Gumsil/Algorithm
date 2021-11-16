n = list(map(int, input()))

# 자릿수
length = len(n)

left_sum = sum(n[:length // 2])
right_sum = sum(n[length // 2:])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
