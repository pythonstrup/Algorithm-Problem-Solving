# 내 풀이
def solution(msg):
    dict = {chr(x): x-64 for x in range(65, 65+26)}
    dict_number = 27
    n = len(msg)
    count = 0

    answer = []
    # dict 추가 알고리즘
    while n > count:
        i = count+1
        while i <= n and msg[count:i] in dict:
            i += 1

        answer.append(dict[msg[count:i-1]])
        dict[msg[count:i]] = dict_number
        dict_number += 1
        count = i-1

    return answer

## 다른 사람 풀이 1
def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer

## 다른 사람 풀이 2
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))