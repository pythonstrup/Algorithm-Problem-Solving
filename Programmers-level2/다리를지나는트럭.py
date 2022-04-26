# 내 풀이 - 0~86ms
def solution(bridge_length, weight, truck_weights):
    from collections import deque
    truck = deque(truck_weights)
    going = deque()
    time = deque()
    answer = 0

    while truck or going:
        if time:
            if answer - time[0] == bridge_length:
                going.popleft()
                time.popleft()

        if truck:
            if sum(going) + truck[0] <= weight:
                going.append(truck.popleft())
                time.append(answer)

        answer += 1

    return answer

# 다른 풀이
# 속도는 0~46ms
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step


# 다른 풀이2
# 가장 빠른 속도 - 모든 케이스가 0.xx ms
from collections import deque

def solution(bridge_length, weight, truck_weights):
    b, w, t = bridge_length, weight, truck_weights
    time = deque([1])
    wsum = deque([t[0]])
    sec = 0
    for v, i in enumerate(t[1:]):
        if i <= weight - sum(wsum):
                time.append(1)
                wsum.append(i)
                if sum(time) - time[0] == b:
                    sec += time.popleft()
                    wsum.popleft()
                continue
        if i <= weight - sum(wsum) + wsum[0]:
            sec += time.popleft()
            wsum.popleft()
            time.append(b - sum(time))
            wsum.append(i)
            continue
        while i > weight - sum(wsum):
            sec += time.popleft()
            wsum.popleft()
        time.append(b - sum(time))
        wsum.append(i)
    for i in time:
        sec += i
    return sec + b

print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))