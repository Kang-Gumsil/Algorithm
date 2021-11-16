k, p, n = map(int, input().split())

result = k * (p ** n)
print(result % 1000000007)