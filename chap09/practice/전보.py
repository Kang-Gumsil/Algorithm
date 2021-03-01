import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        # 이미 처리한 도시는 패스
        if distance[now] < dist:
            continue

        for f_now, f_dist in graph[now]:
            new_dist = dist + f_dist

            if new_dist < distance[f_now]:
                distance[f_now] = new_dist
                heapq.heappush(q, (new_dist, f_now))


# 도시의 개수 n, 통로의 개수 m, 메시지를 보낼 도시 c 입력받기
n, m, c = map(int, input().split())

# 그래프 초기화 및 입력 받기
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2, dist = map(int, input().split())
    graph[v1].append((v2, dist))

# 최단거리 테이블 초기화
distance = [INF] * (n + 1)

# 다익스트라 알고리즘 수행
dijkstra(c)

# 결과 도출 및 출력
dists = [dist for dist in distance if dist != INF]
n_city = len(dists) - 1
max_time = max(dists)

print("%d %d" % (n_city, max_time))


