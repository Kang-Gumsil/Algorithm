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


v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    v1, v2, cost = map(int, input().split())
    edges.append((v1, v2, cost))

edges.sort(key=lambda x: x[2])

for v1, v2, cost in edges:
    if find_parent(parent, v1) != find_parent(parent, v2):
        union_parent(parent, v1, v2)
        result += cost

print(result)
