

# 다른 사람 풀이 - bfs(너비) 사용
from collections import deque

def bfs(start, visited, graph):
    queue = deque([start])
    result = 1
    visited[start] = True

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if visited[i] == False:
                result += 1
                queue.append(i)
                visited[i] = True

    return result

def solution(n, wires):

    answer = n
    graph = [[] for _ in range(n+1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for start, not_visit in wires:
        visited = [False]*(n+1)
        visited[not_visit] = True
        result = bfs(start, visited, graph)
        if abs(result-(n-result)) < answer:
            answer = abs(result - (n-result))

    return answer

# 다른 사람 풀이 - dfs(깊이) 사용
from collections import defaultdict

def dfs(start, visit):
    global count
    visit.append(start)
    count += 1
    for i in tree[start]:
        if i not in visit:
            dfs(i, visit)


def solution(n, wires):
    global tree, count
    result = []
    tree = defaultdict(list)
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)

    for a, b in wires:
        tree[a].remove(b)
        tree[b].remove(a)
        count = 0
        dfs(1, [])
        result.append(abs(n - (count * 2)))
        tree[a].append(b)
        tree[b].append(a)

    return min(result)


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))