import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijstra(start, end):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]

path1 = dijstra(1, v1) + dijstra(v1, v2) + dijstra(v2, n)
path2 = dijstra(1, v2) + dijstra(v2, v1) + dijstra(v1, n)
result = min(path1, path2)

if result >= INF:
    print(-1)
else:
    print(result)
