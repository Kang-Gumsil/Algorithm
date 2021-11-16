# def find_parent(parent, x):
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
