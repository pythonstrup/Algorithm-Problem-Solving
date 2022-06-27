
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

# 내 풀이
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for index, value in enumerate(priorities):
        queue.append((index, value))

    queue.append((0, 0))  # 더미값 입력

    while queue:
        temp = queue.popleft()
        if max(queue, key=lambda x: x[1])[1] <= temp[1]:
            answer += 1
            if temp[0] == location:
                break
        else:
            queue.append(temp)

    return answer

# 다른 사람 풀이 1
def solution(priorities, location):
    jobs = len(priorities)
    answer = 0
    cursor = 0
    while True:
        if max(priorities) == priorities[cursor%jobs]:
            priorities[cursor%jobs] = 0
            answer += 1
            if cursor%jobs == location:
                break
        cursor += 1
    return answer

# p = [2, 1, 3, 2]
# l = 2
# print(solution(p, l))

p = [1, 1, 9, 1, 1, 1]
l = 0
print(solution(p, l))
