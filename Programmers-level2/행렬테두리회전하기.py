
def solution(rows, columns, queries):
    graph = [[(j+1) + i*rows for j in range(columns)] for i in range(rows)]
    answer = []

    for query in queries:
        query = [x-1 for x in query]
        x1, y1, x2, y2 = query
        tmp = graph[x1][y1]
        small = tmp

        for i in range(x1+1, x2+1):
            graph[i-1][y1] = graph[i][y1]
            small = min(small, graph[i][y1])
        for i in range(y1+1, y2+1):
            graph[x2][i-1] = graph[x2][i]
            small = min(small, graph[x2][i])
        for i in range(x2-1, x1-1, -1):
            graph[i+1][y2] = graph[i][y2]
            small = min(small, graph[i][y2])
        for i in range(y2-1, y1-1, -1):
            graph[x1][i+1] = graph[x1][i]
            small = min(small, graph[x1][i])
        graph[x1][y1+1] = tmp

        answer.append(small)

    return answer

q = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(6, 6, q))

# q = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
# print(solution(3, 3, q))
#
# q = [[1,1,100,97]]
# print(solution(100, 97, q))