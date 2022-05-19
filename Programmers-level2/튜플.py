# 내 풀이 - 최대 270ms 정도
def solution(s):
    arr = [c.split(',') for c in s[2:-2].split('},{')]
    arr.sort(key=len)

    answer = []
    for i, v in enumerate(arr):
        for j in v:
            if int(j) not in answer:
                answer.append(int(j))

    return answer

# 다른 사람 풀이1 - 정규표현식사용: 최대 38.5ms
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))