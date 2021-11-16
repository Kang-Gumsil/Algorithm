import sys
input = sys.stdin.readline

k, n = map(int, input().split())

d = [0] * (n + 1)
time = [0] * (n + 1)
move = [0] * (n + 1)

for i in range(1, n):
    data = list(map(int, input().split()))
    time[i], move[i] = [0] + data[:k], [0] + data[k]
time[n] = [0] + list(map(int, input().split()))

# 첫 번째 조립
min_time = min(time[1][1:])
idx = time[1].index(min_time)
d[1] = (min_time, idx)


# 2 ~ n번째 조립
for i in range(2, n + 1):
    now_idx = d[i - 1][1]

    # 이동시 최소값
    min_time_move = min(time[i][1:]) + move[i - 1]
    min_time_idx = time[i].index(min(time[i][1:]))

    # 비교
    if min_time_move < time[i][now_idx]:
        d[i] = (min_time_move + d[i - 1][0], min_time_idx)
    else:
        d[i] = (time[i][now_idx] + d[i - 1][0], now_idx)

print(d[n][0])
