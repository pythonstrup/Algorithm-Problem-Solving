# 내 풀이
from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    distance = [0] * (n+1)

    graph = [[] for i in range(n+1)] #각 노드에 연결된 노드 정보 저장

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    queue = deque()
    queue.append(1)
    visited[1] = True
    while queue:
        temp = queue.popleft()

        for i in graph[temp]:
            if not visited[i]:
                distance[i] = distance[temp] + 1
                queue.append(i)
                visited[i] = True

    max_value = max(distance)

    return distance.count(max_value)