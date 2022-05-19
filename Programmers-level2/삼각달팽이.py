# 내 풀이
def solution(n):
    answer = [[1]*i for i in range(1, n+1) ]
    a = 0
    b = 0
    num = 1
    for i in range(n, 0, -3):
        for j in range(i):
            answer[a][b] = num
            a += 1
            num += 1
        a -= 1
        for j in range(i-1):
            b += 1
            answer[a][b] = num
            num += 1
        for j in range(i-2):
            a -= 1; b -= 1
            answer[a][b] = num
            num += 1
        a += 1

    import itertools
    return list(itertools.chain.from_iterable(answer))

# 다른 사람 풀이 1
def solution(n):
    import itertools
    answer = [[1] * i for i in range(1,n+1)]

    row = -1; col = 0
    num = 1
    for i in range(n, 0, -3):
        for j in range(i):
            row += 1
            answer[row][col] = num
            num += 1
        for j in range(i-1):
            col += 1
            answer[row][col] = num
            num += 1
        for j in range(i-2):
            row -= 1
            col -= 1
            answer[row][col] = num
            num += 1

    return list(itertools.chain(*answer))

# 다른 사람 풀이 2
def solution(n):
    dx=[0,1,-1];dy=[1,0,-1]
    b=[[0]*i for i in range(1,n+1)]
    x,y=0,0;num=1;d=0
    while num<=(n+1)*n//2:
        b[y][x]=num
        ny=y+dy[d];nx=x+dx[d];num+=1
        if 0<=ny<n and 0<=nx<=ny and b[ny][nx]==0:y,x=ny,nx
        else:d=(d+1)%3;y+=dy[d];x+=dx[d]
    return sum(b,[])

print(solution(4))
print(solution(5))
print(solution(6))