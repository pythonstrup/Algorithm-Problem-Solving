# 내 풀이
answer = 0

def dfs(computers, v, visited, n):
    global answer
    if visited[v] == 0:
        answer += 1
        visited[v] = 1

    for i in range(n):
        if computers[v][i] == 1 and not visited[i]:
            visited[i] = 1
            dfs(computers, i, visited, n)


def solution(n, computers):
    visited = [0] * (n)

    for i in range(n):
        dfs(computers, i, visited, n)

    return answer

# 개선한 내 풀이 - 전역변수를 제거 및 dfs를 간소화
def dfs(computers, v, visited, n):
    visited[v] = 1

    for i in range(n):
        if computers[v][i] == 1 and not visited[i]:
            dfs(computers, i, visited, n)


def solution(n, computers):
    visited = [0] * n
    answer = 0

    for i in range(n):
        if visited[i] == 0:
            dfs(computers, i, visited, n)
            answer += 1

    return answer


# 다른 사람 풀이1
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer


# 다른 사람 풀이2
def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))