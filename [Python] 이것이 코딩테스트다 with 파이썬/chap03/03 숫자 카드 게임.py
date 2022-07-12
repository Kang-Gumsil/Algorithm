n, m = map(int, input().split())

result = -1
for _ in range(n):
    data = list(map(int, input().split()))
    min_data = sorted(data)[0]
    result = max(min_data, result)

print(result)
