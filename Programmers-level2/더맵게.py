import heapq

def solution(scoville, k):
    answer = 0

    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while heap[0] < k:
        if len(heap) > 1:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap)*2))
            answer += 1
        else:
            return -1

    return answer

# sco = [1, 2, 3, 9, 10, 12]
# k = 7
# print(solution(sco, k))

sco = [3, 1, 4]
k = 5
print(solution(sco, k))

# sco = [0, 0, 0, 1, 4]
# k = 7
# print(solution(sco, k))

