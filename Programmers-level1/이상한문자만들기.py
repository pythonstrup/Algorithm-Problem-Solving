def solution(s):
    answer = ""
    arr = s.split(" ")

    for word in arr:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()

        answer += " "

    return answer[:-1]

print(solution("try hello world"))