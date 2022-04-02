def solution(s):
    answer = s
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(10):
        if words[i] in answer:
            answer = answer.replace(words[i], str(i))

    return int(answer)



s = "23zero4zero"
print(solution(s))
