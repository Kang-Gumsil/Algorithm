def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x1, x2):
    x1 = find_parent(parent, x1)
    x2 = find_parent(parent, x2)

    if x1 > x2:
        parent[x1] = x2
    else:
        parent[x2] = x1


# n: 학생 수
# m: 수행 가능한 연산의 수
n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    op, s1, s2 = map(int, input().split())

    if op == 0:    # 팀 합치기
        union_parent(parent, s1, s2)

    else:    # 같은 팀 여부 확인
        if find_parent(parent, s1) == find_parent(parent, s2):
            print("YES")
        else:
            print("NO")