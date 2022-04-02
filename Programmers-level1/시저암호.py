def solution(s, n):
    answer = ''
    for char in s:
        if char.islower():
            char = chr((ord(char)-ord('a')+n) % 26 + ord('a'))
        elif char.isupper():
            char = chr((ord(char)-ord('A')+n) % 26 + ord('A'))

        answer += char
    return answer


print(solution("ABX", 6))
print(solution("z", 1))
print(solution("a B z", 4))
