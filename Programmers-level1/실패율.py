# def solution(N, stages):
#     dict = {}
#     answer = []
#     cnt = len(stages)
#     for i in range(1, N+1):
#         dict[i] = stages.count(i)
#         answer.append(i)
#
#     for i in range(1, N+1):
#         if cnt == 0:
#             break
#         else:
#             dict[i] = dict[i] / cnt
#             cnt -= stages.count(i)
#
#     answer = sorted(answer, key=lambda x: dict[x], reverse=True)
#     return answer


### 제일 많은 풀이 ###
# def solution(N, stages):
#     result = {}
#     denominator = len(stages)
#     for stage in range(1, N+1):
#         if denominator != 0:
#             count = stages.count(stage)
#             result[stage] = count / denominator
#             denominator -= count
#         else:
#             result[stage] = 0
#     return sorted(result, key=lambda x : result[x], reverse=True)


## 효율성 제일 좋은 풀이 ##
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    print(info)
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append(((i + 1), 0))
        else:
            fail.append(((i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(item[0])
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))