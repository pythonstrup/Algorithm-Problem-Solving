from collections import deque

n, k = map(int, input().split())
range = 100_000
distance = [0] * (range+1)

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        now = queue.popleft()
        if now == k:
            print(distance[now])
            break
        for i in (now-1, now+1, now*2):
            if 0 <= i <= range and not distance[i]:
                distance[i] = distance[now] + 1
                queue.append(i)

bfs()