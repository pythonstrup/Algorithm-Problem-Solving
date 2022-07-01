# 내 풀이 - 0.00~0.48
def solution(begin, target, words):
    n = len(begin)
    length = len(words)
    is_complete = False
    answer = []
    result = []
    visited = [0] * length

    if target not in words:
        return 0

    def dfs(word):
        dif1 = 0
        for i in range(n):
            if word[i] != target[i]:
                dif1 += 1

        if dif1 == 1:
            is_complete = True
            answer.append(result[:])

        for i in range(length):
            if visited[i]:
                continue

            dif2 = 0
            for j in range(n):
                if word[j] != words[i][j]:
                    dif2 += 1

            if dif2 == 1:
                visited[i] = True
                result.append(words[i])
                dfs(words[i])
                result.pop()
                visited[i] = False

    dfs(begin)
    min_length = 9999
    for i in answer:
        l = len(i)
        if min_length > l:
            min_length = l
            print(i)

    return min_length + 1

# 내 풀이 정리: 반복되는 부분을 함수화
def get_difference(word1, word2, n):
    dif = 0
    for i in range(n):
        if word1[i] != word2[i]:
            dif += 1

    return dif

def solution(begin, target, words):
    n = len(begin)
    length = len(words)
    answer = []
    result = []
    visited = [0] * length

    if target not in words:
        return 0

    def dfs(word):
        dif1 = get_difference(word, target, n)

        if dif1 == 1:
            answer.append(result[:])

        for i in range(length):
            if visited[i]:
                continue

            dif2 = get_difference(word, words[i], n)
            if dif2 == 1:
                visited[i] = True
                result.append(words[i])
                dfs(words[i])
                result.pop()
                visited[i] = False

    dfs(begin)
    min_length = 9999
    for i in answer:
        l = len(i)
        if min_length > l:
            min_length = l
            print(i)

    return min_length + 1


# 다른 사람 풀이1 - bfs사용: 0.01~0.48
# 성능은 거의 동일
from collections import deque

def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)


# 내코드랑 길이는 비슷하지만 성능은 더 좋음
from collections import defaultdict

def nextWord(cur, words):
    ret = []
    for word in words:
        cnt = 0
        for idx in range(len(word)):
            if word[idx] == cur[idx]:
                cnt += 1
        if cnt == len(cur)-1:
            ret.append(word)
    return ret

def bfs(begin, target, words):
    visited = defaultdict(lambda: False)
    queue = nextWord(begin, words)
    count = 0
    min = 1e9

    while(len(queue) > 0):
        size = len(queue)
        count += 1

        for _ in range(size):
            key = queue.pop(0)
            visited[key] = True
            if (key == target and count < min):
                min = count
            for candidate in nextWord(key, words):
                if (visited[candidate] == False):
                    queue.append(candidate)

    if min == 1e9:
        return 0
    else:
        return min

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer