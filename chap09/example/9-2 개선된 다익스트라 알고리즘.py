import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []  # 큐로 사용할 리스트
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        # 현재 노드가 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue

        for node, cost in graph[now]:
            new_cost = dist + cost

            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(q, (new_cost, node))


# n: 노드의 개수 / m: 간선의 개수
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))

dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print(-1)
    else:
        print(distance[i])
