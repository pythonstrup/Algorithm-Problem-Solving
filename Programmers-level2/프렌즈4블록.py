# 내풀이.. 무식한 방법
def solution(m, n, board):
    answer = 0
    # 오른쪽과 아래 방향으로 점자 검색해간다.
    x = [1, 0, 1]
    y = [1, 1, 0]

    new_board = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(board[i][j])
        new_board.append(temp)

    phase = True
    while phase:
        phase = False
        temp = []  # 한 턴에 지울 좌표값
        for i in range(m - 1):
            for j in range(n - 1):
                if new_board[i][j] == "":
                    continue

                elif new_board[i][j] == new_board[i + 1][j + 1] == new_board[i + 1][j] == new_board[i][j + 1]:
                    phase = True
                    temp.append([i, j])
                    temp.append([i + 1, j + 1])
                    temp.append([i + 1, j])
                    temp.append([i, j + 1])

        for pos in temp:
            if new_board[pos[0]][pos[1]] == "":
                continue  # 중복해서 들어간 값을 제외함

            answer += 1
            new_board[pos[0]][pos[1]] = ""

        for j in range(n):
            for k in range(m - 1):
                for i in range(m - k - 1):
                    if new_board[i + 1][j] == "":
                        new_board[i + 1][j], new_board[i][j] = new_board[i][j], new_board[i + 1][j]

    return answer

# 다른 사람 풀이 1 - 내 풀이보다 훨씬 빠르다.
def pop_num(b, m, n):
    pop_set = set()
    # search
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] == b[i - 1][j - 1] == b[i - 1][j] == b[i][j - 1] != '_':
                pop_set |= set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])
    # set_board
    for i, j in pop_set:
        b[i][j] = 0
    for i, row in enumerate(b):
        empty = ['_'] * row.count(0)
        b[i] = empty + [block for block in row if block != 0]
    return len(pop_set)


def solution(m, n, board):
    count = 0
    b = list(map(list, zip(*board)))  # 행열 바꿔치기
    while True:
        pop = pop_num(b, m, n)
        if pop == 0: return count
        count += pop


# 다른 사람 풀이 2 - 내 풀이보다 약간 빠름
def pang(m, n, board):
    t_board = []
    for x in range(m):
        t_board.append([])
        for y in range(n):
            t_board[x].append(board[x][y])

    flag = False
    for x in range(m-1):
        for y in range(n-1):
            if len(set([board[x][y], board[x][y+1], board[x+1][y], board[x+1][y+1]])) == 1:
                if board[x][y] != '0':
                    flag = True
                    t_board[x][y] = '0'
                    t_board[x][y+1] = '0'
                    t_board[x+1][y] = '0'
                    t_board[x+1][y+1] = '0'

    return flag, t_board


def restruct(m, n, board):
    re_board = [''] * m
    for x in range(n):
        ys = ''.join([board[y][x] for y in range(m)]).replace('0','').zfill(m)
        for y in range(m):
            re_board[y] += ys[y]

    return re_board


def get_num(m, n, board):
    cnt = 0
    for x in range(m):
        for y in range(n):
            if board[x][y] == '0':
                cnt += 1
    return cnt

def solution(m, n, board):
    flag = True
    while flag:
        flag, board = pang(m, n, board)
        board = restruct(m, n, board)

    return get_num(m, n, board)