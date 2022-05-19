# 내 코드
def solution(n, words):
    last = ''
    already = []
    for i, v in enumerate(words):
        if i == 0:
            last = v[-1]
        else:
            if last != v[0] or v in already:
                return [(i%n) + 1, (i//n)+1]
            last = v[-1]
        already.append(v)
    return [0, 0]

# 다른 사람 풀이 1
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish",
                   "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))