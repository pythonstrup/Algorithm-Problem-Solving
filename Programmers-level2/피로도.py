# 내 풀이 - 백트래킹 사용
def solution(k, dungeons):
    global answer
    n = len(dungeons)
    visited = [False] * n
    result = []
    answer = 0

    def dfs():
        global answer
        if len(result) == n:
            limit = k
            an = 0
            for step in result:
                if limit >= step[0] and limit >= step[1]:
                    an += 1
                    limit -= step[1]
            answer = max(answer, an)

        for i in range(n):
            if visited[i]:
                continue

            visited[i] = True
            result.append(dungeons[i])
            dfs()
            result.pop()
            visited[i] = False

    dfs()
    return answer

# 다른 사람 풀이 1 - 백트래킹: 내 것보다 훨씬 효율적
answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer

# 다른 사람 풀이 2 - 이제는 테스트 케이스 18, 19 실패
def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key = lambda x : ((x[1]+x[0])/x[0],x[1]))
    for x,y in dungeons:
        print("x :", x, "y : ", y)
        if k >= x:
            k -= y
            answer += 1
    return answer

# 다른 사람 풀이 3 - 순열 사용
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for case in permutations(dungeons):
        t = 0; p = k
        for d in case:
            if d[0]<=p:
                p-=d[1]; t += 1
            else: break
        answer = max(answer, t)
        if answer == len(dungeons): break
    return answer

# 다른 사람 풀이 - 한 줄 코드
solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])

print(solution(80, [[80,20],[50,40],[30,10]]))
print(solution(30, [[50,20],[80,40],[30,10]]))