# 내 풀이
import math

def decimal_to_k(n, k):
    stack = []
    while True:
        if n == 0:
            break
        stack.append(n % k)
        n //= k

    stack.reverse()
    return stack

def is_prime_number(x):
    if x <= 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    con = decimal_to_k(n, k)
    con = "".join(list(map(str, con)))
    arr = con.split('0')
    answer = 0
    for num in arr:
        if num and is_prime_number(int(num)):
            print(num)
            answer += 1
    return answer