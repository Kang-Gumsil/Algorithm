from collections import deque

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

result = 0
def bfs(x, y):

    if x < 0 or x >= m or y < 0 or y >= n:
        return False

