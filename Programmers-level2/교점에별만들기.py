# 내 풀이1 - 오답 (33점)
def solution(line):
    answer = []

    pos = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a = line[i][0]; b = line[i][1]; e = line[i][2]
            c = line[j][0]; d = line[j][1]; f = line[j][2]
            if a*d - b*c == 0:
                continue

            xpos = (b*f-e*d)/(a*d-b*c)
            ypos = (e*c-a*f)/(a*d-b*c)
            # 정수인지 확인
            if xpos - int(xpos) == 0 and ypos - int(ypos) == 0:
                pos.append((int(xpos), int(ypos)))

    pos = list(set(pos))  # 중복 제거
    pos.sort()
    x_min = pos[0][0]
    x_max = pos[-1][0]
    pos.sort(key=lambda x: x[1])
    y_min = pos[0][1]
    y_max = pos[-1][1]

    for i in range(y_max-y_min, -1, -1):
        temp = ""
        for j in range(x_max-x_min, -1, -1):
            if (j+x_min, i+y_min) in pos:
                temp += "*"
            else:
                temp += "."
        answer.append(temp)

    return answer

# 내 풀이 2 - 정답
def solution(line):
    pos = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a = line[i][0]; b = line[i][1]; e = line[i][2]
            c = line[j][0]; d = line[j][1]; f = line[j][2]
            if a*d - b*c == 0:
                continue

            xpos = (b*f-e*d)/(a*d-b*c)
            ypos = (e*c-a*f)/(a*d-b*c)
            # 정수인지 확인
            if xpos - int(xpos) == 0 and ypos - int(ypos) == 0:
                pos.append((int(xpos), int(ypos)))

    pos = list(set(pos))  # 중복 제거
    pos.sort()
    x_min = pos[0][0]
    x_max = pos[-1][0]
    pos.sort(key=lambda x: x[1])
    y_min = pos[0][1]
    y_max = pos[-1][1]

    answer = [['.']*(abs(x_max-x_min)+1) for _ in range(abs(y_max-y_min)+1)]
    for p in pos:
        a, b = p
        x, y = abs(y_max-b), abs(x_min-a)
        answer[x][y] = "*"
    for index, value in enumerate(answer):
        answer[index] = "".join(value)

    return answer

# 내 풀이3 - 정답
def solution(line):
    answer = []

    pos = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a = line[i][0]; b = line[i][1]; e = line[i][2]
            c = line[j][0]; d = line[j][1]; f = line[j][2]
            if a*d - b*c == 0:
                continue

            xpos = (b*f-e*d)/(a*d-b*c)
            ypos = (e*c-a*f)/(a*d-b*c)
            # 정수인지 확인
            if xpos - int(xpos) == 0 and ypos - int(ypos) == 0:
                pos.append((int(xpos), int(ypos)))

    pos = list(set(pos))  # 중복 제거
    pos.sort()
    x_min = pos[0][0]
    x_max = pos[-1][0]
    pos.sort(key=lambda x: x[1])
    y_min = pos[0][1]
    y_max = pos[-1][1]

    for i in range(y_max, y_min-1, -1):
        temp = ""
        for j in range(x_min, x_max+1):
            if (j, i) in pos:
                temp += "*"
            else:
                temp += "."
        answer.append(temp)

    return answer

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))