def solution(dartResult):
    answer = []
    score = [0, "S", "D", "T"]
    result = 0
    for idx, char in enumerate(dartResult):
        if dartResult[idx-1].isdigit() and char == "0":
            continue

        if char.isdigit():
            if dartResult[idx+1] == '0':
                char += '0'
            answer.append(result)
            result = int(char)

        elif char.isalpha():
            result **= score.index(char)

        else:
            if char == "*":
                result *= 2
                answer[-1] *= 2
            else:
                result *= (-1)

    answer.append(result)
    return sum(answer)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S3T*"))
print(solution("1S*2T*3S"))
print(solution("1T2D3D#"))
print(solution("10D4S10D"))

