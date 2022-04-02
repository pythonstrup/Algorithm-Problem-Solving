
def solution(a, b):
    n = a
    m = b
    answer = []
    while n != m:
        if n > m: n-=m
        else: m-=n

    answer.append(n)
    answer.append((a*b)//n)
    return answer

