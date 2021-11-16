INF = int(1e3)

# 노드 및 간선 개수 입력받기
n = int(input())
m = int(input())

# 그래프 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

# 그래프 입력받기
for _ in range(m):
    v1, v2, dist = map(int, input().split())
    graph[v1][v2] = dist

# 플루이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print("INF", end=' ')
        else:
            print(" %d " % graph[i][j], end=' ')
    print()
