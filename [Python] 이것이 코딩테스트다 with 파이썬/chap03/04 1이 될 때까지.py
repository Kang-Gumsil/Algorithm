n, k = map(int, input().split())

count = 0
while n >= k:
    count += n % k + 1
    n //= k
count += n - 1

print(count)
