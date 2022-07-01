# 내 풀이 - 최대 1.3ms
import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    heap = []
    jobs.sort(reverse=True)

    complete = 0
    second = 0
    while complete < n:
        while jobs:
            if jobs[-1][0] > second:
               break
            temp = jobs.pop()
            heapq.heappush(heap, [temp[1], temp[0]])

        if heap and heap[0][1] <= second:
            temp = heapq.heappop(heap)
            answer += temp[0] + second - temp[1]
            complete += 1
            second += temp[0]
        else:
            second += 1
        print(answer)

    return answer//n


# 다른 사람 풀이1
# 내 것보다 성능 약 1.5배 가량 좋음
import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)

# 다른 사람 풀이2
# 내 풀이보다 성능 약간 안 좋음
import heapq


class Job(object):
    def __init__(self, begin=0, cost=0):
        self.begin = begin
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost


def solution(jobs):
    jobs.sort(key=lambda item: item[0])

    last_index = 1
    job_heap = [Job(begin=jobs[0][0], cost=jobs[0][1])]
    current_time = jobs[0][0]
    answer = 0
    while True:
        while last_index < len(jobs) and jobs[last_index][0] <= current_time:
            job = Job(begin=jobs[last_index][0], cost=jobs[last_index][1])
            heapq.heappush(job_heap, job)
            last_index += 1

        if len(job_heap) == 0:
            if last_index < len(jobs):
                job = Job(begin=jobs[last_index][0], cost=jobs[last_index][1])
                current_time = job.begin
                heapq.heappush(job_heap, job)
                last_index += 1
            else:
                break

        next_job = heapq.heappop(job_heap)

        current_time += next_job.cost

        answer += (current_time - next_job.begin)

    answer = int(answer/len(jobs))
    return answer

# 다른 사람 풀이 3
# 내 풀이보다 성능 5배 나쁨 - 최대 8ms
import heapq
def solution(jobs):
    answer = 0
    end, i = 0, 0
    start = -1
    hq = []
    while len(jobs)>i:
        for job in jobs:
            if start<job[0]<=end:
                heapq.heappush(hq, (job[1], job[0]))
        if len(hq)>0:
            now = heapq.heappop(hq)
            start = end
            end += now[0]
            answer += (end-now[1])
            i += 1
        else:
            end+=1
    answer = answer//len(jobs)
    return answer