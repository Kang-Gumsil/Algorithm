n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first, second = data[0], data[1]

repeat, margin = m // (k + 1), m % (k + 1)
result = repeat * (k * first + second) + margin * first

print(result)
