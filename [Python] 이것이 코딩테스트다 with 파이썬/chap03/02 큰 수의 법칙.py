# 입력 받기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 내림차순으로 정렬
data.sort(reverse=True)
first = data[0]
second = data[1]

# 더하기
repeat, margin = m // (k + 1), m % (k + 1)
result = (first * k + second) * repeat + first * margin

# 출력
print(result)
