# 내 풀이
def solution(skill, skill_trees):
    answer = 0

    for s in skill_trees:
        idx = 0
        for c in s:
            if c in skill:
                if c == skill[idx]:
                    idx += 1
                else:
                    answer -= 1
                    break
        answer += 1

    return answer

## 다른 사람 풀이
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))