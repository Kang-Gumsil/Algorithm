n, m = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

min_values = []
for values in data:
    min_values.append(min(values))

print(max(min_values))

