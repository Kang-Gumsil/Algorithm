import sys
input = sys.stdin.readline
INF = int(1e9)

# n, m 입력받기
n, m = map(int, input().split())

# 그래프 초기화 및 입력받기
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

# x, k 입력받기
x, k = map(int, input().split())

# 플루이드 워셜 알고리즘 수행
for m in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][m] + graph[m][j])

# 결과 출력
if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])

