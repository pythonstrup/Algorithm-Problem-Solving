# 내풀이
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    # priority = deque()

    for city in cities:
        city = city.lower()
        if len(cache) == cacheSize:
            if city in cache:
                answer += 1
                cache.remove(city)
                cache.appendleft(city)
            elif cacheSize != 0:
                answer += 5
                cache.pop()
                cache.appendleft(city)
            else:
                answer += 5
        else:
            if city in cache:
                answer += 1
                cache.remove(city)
                cache.appendleft(city)
            else:
                answer += 5
                cache.appendleft(city)

    return answer

# 내 풀이 단순하게 정리
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.appendleft(city)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.pop()
            cache.appendleft(city)

    return answer

# 다른 사람 풀이1
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time