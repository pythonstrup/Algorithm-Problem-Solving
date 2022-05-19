# 내 풀이
def gcd(a, b):
    if a < b:
        a, b = b, a

    while a % b:
        a, b = b, a % b

    return b

def solution(w,h):
    return w * h - (w + h - gcd(w, h))


# 다른 사람 풀이 1
def gcd(a,b): return b if (a==0) else gcd(b%a,a)
def solution(w,h): return w*h-w-h+gcd(w,h)


# 다른 사람 풀이 2
from math import gcd
def solution(w,h):
    return w * h - (w/gcd(w, h) + h/gcd(w, h) - 1) * gcd(w, h)

print(solution(8, 12))
print(solution(6, 4))