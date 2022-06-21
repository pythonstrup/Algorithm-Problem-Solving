# 내 풀이
def solution(dirs):
    d = ["U", "D", "R", "L"]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visit = set()

    my_pos = [0, 0]
    for c in dirs:
        for i in range(4):
            if d[i] == c:
                nx = my_pos[0] + dx[i]
                ny = my_pos[1] + dy[i]

                if -5 <= nx <= 5 and -5 <= ny <= 5:
                    visit.add((my_pos[0], my_pos[1], nx, ny))
                    visit.add((nx, ny, my_pos[0], my_pos[1]))
                    my_pos = [nx, ny]

    return len(visit) // 2

# 다른 사람 풀이 1
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2

# 다른 사람 풀이 2
def solution(dirs):
    answer = 0
    X = []
    Y = []
    for i in range(11):
        X.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])
        Y.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])

    point = [0, 0]

    for i in range(len(dirs)):
        if dirs[i] == 'U' and point[1] != 5:
            if Y[point[0] + 5][point[1] + 5] != 1:
                Y[point[0] + 5][point[1] + 5] = 1
                answer += 1
            point[1] += 1
        elif dirs[i] == 'D' and point[1] != -5:
            if Y[point[0] + 5][point[1] + 4] != 1:
                Y[point[0] + 5][point[1] + 4] = 1
                answer += 1
            point[1] -= 1
        elif dirs[i] == 'R' and point[0] != 5:
            if X[point[1] + 5][point[0] + 5] != 1:
                X[point[1] + 5][point[0] + 5] = 1
                answer += 1
            point[0] += 1
        elif dirs[i] == 'L' and point[0] != -5:
            if X[point[1] + 5][point[0] + 4] != 1:
                X[point[1] + 5][point[0] + 4] = 1
                answer += 1
            point[0] -= 1
    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))