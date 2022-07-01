# 내 풀이
from itertools import product

def solution(word):
    arr = ["A", "E", "I", "O", "U"]
    result = []
    for i in range(1, 6):
        result.extend(list(product(arr, repeat=i)))


    result.sort()
    dict = {}
    for i, value in enumerate(result):
        dict["".join(value)] = i+1

    return dict[word]

# 내 풀이 변형 - dict를 만들지 않고 바로 찾기
# 1ms정도 성능 더 좋아짐
def solution(word):
    from itertools import product
    arr = ["A", "E", "I", "O", "U"]
    result = []
    for i in range(1, 6):
        result.extend(list(product(arr, repeat=i)))

    result.sort()
    for i, value in enumerate(result):
        if "".join(value) == word:
            return i+1

# 수학적인 풀이: 성능 최상 0.01ms
# 등비수열 사용
def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer

# 내풀이보다 약간 빠름
from itertools import product

solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1