# 내풀이 - 중복조합 사용
from itertools import combinations_with_replacement

def scoring(list1, list2):
    score1 = 0
    score2 = 0
    for i in range(11):
        if list1[i] > list2[i]:
            score1 += 10-i
        elif list2[i] == 0:
            continue
        else:
            score2 += 10-i

    return score1 - score2

def compare(list1, list2):
    return list1[::-1] > list2[::-1]

def solution(n, info):

    select = [x for x in range(10, -1, -1)]
    cases = list(combinations_with_replacement(select, n))

    score = 0 # index & score
    answer = [0] * 12
    for shot in cases:
        result = [0] * 12
        for i in shot:
            result[10-i] += 1

        s = scoring(result, info)
        result[11] = s
        if s >= score:
            score = s
            if compare(result, answer): answer = result[:]

    return [-1] if score == 0 else answer[:-1]


# 다른 사람의 풀이 - 중복 조합을 이용한 더 간략한 풀이
from itertools import *

# a가 b보다 더 좋은 배치일 경우 true
def cmp(a, b):
    return a[::-1] > b[::-1]

def solution(n, info):
    # 라이언이 가장 큰 점수 차이로 우승할 수 있는 결과를 저장
    # ret[0..10] : 10-i점에서 라이언이 맞힌 화살의 수, ret[11] : 점수 차이
    ret = [-1] * 12 
    for comb in combinations_with_replacement(range(11), n):
        arrow = [0] * 12
        score = 0
        for x in comb: arrow[x] += 1
        for i in range(11):
            if arrow[i] > info[i]:
                score += (10 - i)
            elif info[i] != 0:
                score -= (10 - i)
        if score <= 0: continue
        arrow[11] = score
        if cmp(arrow, ret):
            ret = arrow[:] # deepcopy를 해야 함에 주의
    if ret[0] == -1: return [-1]
    return ret[:-1]

# 다른 사람 풀이2 - 백트래킹
import copy
answer = []
maxV = 1

def cal(L, A):
    apeach, lion = 0, 0
    for idx in range(11):
        if A[idx] == 0 and L[idx] == 0:
            continue
        elif A[idx] < L[idx]:
            lion += (10 - idx)
        else:
            apeach += (10 - idx)
    return lion - apeach

def compare(res, L):
    global answer, maxV

    if maxV < res:
        answer = [copy.deepcopy(L)]
        maxV = res
    elif maxV == res:
        answer.append(copy.deepcopy(L))

# solution 1
def solution(n, info):
    global answer

    def score(s, L, cnt):

        if cnt == 11:
            if sum(L) == n:
                compare(cal(L, info), L)

            elif sum(L) < n:
                L[10] += n - sum(L)
                compare(cal(L, info), L)
                L[10] -= n - sum(L)
            return
        for i in range(s, 11):
            L[i] = info[i] + 1
            score(i + 1, L, cnt+1)
            L[i] = 0
            score(i + 1, L, cnt+1)

    score(0, [0] * 11, 0)

    if not answer:
        return [-1]
    answer.sort(key=lambda x: x[::-1])
    return answer[-1]

# 다른 사람 풀이3 - bfs
# 성능은 중복조합보다 훨씬 좋다.
from collections import deque


def bfs(n, info):
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0

    while q:
        focus, arrow = q.popleft()

        if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                    res.clear()
                res.append(arrow)  # 최대점수차를 내는 화살상황 저장

        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏜 경우
            continue

        elif focus == 10:  # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))

        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus] + 1
            q.append((focus + 1, tmp))  # 어피치보다 1발 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus + 1, tmp2))  # 0발 쏘기
    return res


def solution(n, info):
    winList = bfs(n, info)

    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]

# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))