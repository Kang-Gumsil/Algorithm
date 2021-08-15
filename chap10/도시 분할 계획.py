def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, v1, v2):
    v1 = find_parent(parent, v1)
    v2 = find_parent(parent, v2)
    if v1 > v2:
        parent[v1] = v2
    else:
        parent[v2] = v1


# 마을의 개수 n, 도로의 개수 m 입력받고 parent, edges 배열 초기화
n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i
edges = []


# 도로 입력받기
for _ in range(m):
    v1, v2, cost = map(int, input().split())
    edges.append((v1, v2, cost))

# 유지 비용이 낮은 순으로 정렬
edges.sort(key=lambda x: x[2])

# 최종 비용인 total_cost와 최소 신장 트리에 포함된 간선 중 가장 큰 유지비용을 갖는 간선의 비용 max_cost 초기화
total_cost = 0
max_cost = 0

# 유지 비용이 낮은 순서대로 그룹에 합류
# 사이클을 생성할 경우 (= 이미 같은 그룹일 경우) 제외
for v1, v2, cost in edges:
    if find_parent(parent, v1) != find_parent(parent, v2):
        union_parent(parent, v1, v2)
        total_cost += cost
        if cost > max_cost:
            max_cost = cost

# 결과 출력 (그룹을 2개로 분리하기 위해 가장 큰 간선 제외)
print(total_cost - max_cost)
