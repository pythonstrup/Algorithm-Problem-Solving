# 내 풀이
# 크루스칼 알고리즘 사용
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    parent = [0] * (n)
    for i in range(n):
        parent[i] = i

    costs.sort(key=lambda x:x[2])
    for edge in costs:
        a, b, cost = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost

    return answer


# 다른 사람 풀이1 - 크루스칼 알고리즘 변형
def ancestor(node, parents):
    if parents[node] == node:
        return node
    else:
        return ancestor(parents[node], parents)

def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents = [i for i in range(n)]
    bridges = 0
    for w, f, t in edges:
        if ancestor(f, parents) != ancestor(t, parents):
            answer += w
            parents[ancestor(f, parents)] = t
            bridges += 1
        if bridges == n - 1:
            break
    return answer