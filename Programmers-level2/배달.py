# 내 풀이 - 최대 4.5ms
INF = int(1e9)

def choose(n, distance, visited):
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start, distance, visited, graph, n):
    distance[start] = 0
    visited[start] = True
    for v in graph[start]:
        distance[v[0]] = v[1]

    for i in range(n-1):
        now = choose(n, distance, visited)
        visited[now] = True

        for v in graph[now]:
            cost = distance[now] + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost

def solution(N, road, K):
    answer = 0

    graph = [[]*(N+1) for i in range(N+1)]

    for v1, v2, dis in road:
        is_compare = False
        index = 0
        for idx, value in enumerate(graph[v1]):
            if value[0] == v2:
                is_compare = True
                index = idx

        if is_compare:
            if dis >= graph[v1][index][1]:
                continue
            else:
                graph[v1][index][1] = dis
                for idx, value in enumerate(graph[v2]):
                    if value[0] == v1:
                        index = idx
                graph[v2][index][1] = dis
        else:
            graph[v1].append([v2, dis])
            graph[v2].append([v1, dis])

    distance = [INF]*(N+1)
    visited = [0]*(N+1)

    dijkstra(1, distance, visited, graph, N)

    for i in distance:
        if i <= K:
            answer += 1

    return answer

# 내 풀이를 인접행렬로 표현해 개선 - 시간복잡도를 8배 개선함
# 시간복잡도 최대 0.65ms
INF = int(1e9)

def choose(n, distance, visited):
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start, distance, visited, graph, n):
    distance[start] = 0
    visited[start] = True
    for i, v in enumerate(graph[start]):
        distance[i] = v

    for i in range(n - 1):
        now = choose(n, distance, visited)
        visited[now] = True

        for idx, v in enumerate(graph[now]):
            cost = distance[now] + v
            if cost < distance[idx]:
                distance[idx] = cost


def solution(N, road, K):
    answer = 0

    graph = [[INF] * (N + 1) for i in range(N + 1)]

    for v1, v2, dis in road:
        if graph[v1][v2] > dis:
            graph[v1][v2] = dis
            graph[v2][v1] = dis

    for i in range(1, N + 1):
        graph[i][i] = 0

    distance = [INF] * (N + 1)
    visited = [0] * (N + 1)

    dijkstra(1, distance, visited, graph, N)

    for i in distance:
        if i <= K:
            answer += 1

    return answer