# n: 노드의 개수
# m: 간선의 개수
# start: 시작 노드

import sys

input = sys.stdin.readline
INF = int(1e9)


# 방문하지 않은 노드 중에서, 가장 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    result = 0
    min_value = INF

    for i in range(1, n + 1):
        if (distance[i] < min_value) and (not visited[i]):
            result = i
            min_value = distance[i]

    return result


# 다익스트라 알고리즘
def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for v, cost in graph[start]:
        distance[v] = cost

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True

        for v, cost in graph[now]:
            distance[v] = min(distance[v], distance[now] + cost)


n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])