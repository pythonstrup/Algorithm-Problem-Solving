def solution(s):
    stack = []

    for i in s:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    return 0 if stack else 1

print(solution("baabaa"))
print(solution("cdcd"))