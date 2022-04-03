
def solution(priorities, location):
    from collections import deque

    answer = 0
    queue = deque([(i,v) for i, v in enumerate(priorities)])

    while queue:
        temp = queue.popleft()
        if any(temp[1] < q[1] for q in queue):
            queue.append(temp)
        else:
            answer += 1
            if temp[0] == location: break

    return answer

# p = [2, 1, 3, 2]
# l = 2
# print(solution(p, l))

p = [1, 1, 9, 1, 1, 1]
l = 0
print(solution(p, l))
