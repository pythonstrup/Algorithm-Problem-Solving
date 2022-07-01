# 내풀이 - 나머지는 0.01ms, 테스트케이스 1번이 323ms이 되버린다.
def solution(tickets):
    answer = []
    length = len(tickets)
    visited = [0] * length


    def dfs(v, result):
        if len(result) == length:
            temp = []
            for i in result:
                temp.append(i[0])
            temp.append(result[-1][1])
            answer.append(temp[:])

        for i in range(length):
            if visited[i]:
                continue

            if tickets[v][1] == tickets[i][0]:
                visited[i] = True
                result.append(tickets[i])
                dfs(i, result)
                result.pop()
                visited[i] = False


    for i in range(length):
        if tickets[i][0] == "ICN":
            re = []
            visited = [0] * length
            visited[i] = True
            re.append(tickets[i])
            dfs(i, re)

    if len(answer) != 1:
        answer.sort()

    return answer[0]


# 다른 사람 풀이1 - 0.02~0.07ms: 성능우수
from collections import defaultdict

def dfs(graph, N, key, footprint):
    print(footprint)

    if len(footprint) == N + 1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret


def solution(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer


# 다른 사람 풀이2 - 0.01~0.03: 더 우수
def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]


# 더좋은 성능 0.01~0.02
from collections import defaultdict
def solution(tickets):
    r = defaultdict(list)
    for i,j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()

    s = ["ICN"]
    p = []
    while s:
        q = s[-1]
        if r[q] != []:
            s.append(r[q].pop(0))
        else:
            p.append(s.pop())
    return p[::-1]
