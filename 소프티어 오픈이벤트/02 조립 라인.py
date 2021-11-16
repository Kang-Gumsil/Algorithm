n = int(input())

d = [0] * (n + 1)
a = [0] * (n + 1)
b = [0] * (n + 1)
a_to_b = [0] * (n + 1)
b_to_a = [0] * (n + 1)

for i in range(1, n):
    a[i], b[i], a_to_b[i], b_to_a[i] = map(int, input().split())
a[n], b[n] = map(int, input().split())

# 첫 번째 조립 넣기
if a[1] > b[1]:
    d[1] = (b[1], 'b')
else:
    d[1] = (a[1], 'a')

# 2 ~ n 번째 조립 넣기
for i in range(2, n + 1):
    if d[i - 1][1] == 'a':
        x, y = d[i - 1][0] + a[i], d[i - 1][0] + b[i] + a_to_b[i - 1]
        if x > y:
            d[i] = (y, 'b')
        else:
            d[i] = (x, 'a')
    else:
        x, y = d[i - 1][0] + b[i], d[i - 1][0] + a[i] + b_to_a[i - 1]
        if x > y:
            d[i] = (x, 'b')
        else:
            d[i] = (y, 'a')

print(d[n][0])
