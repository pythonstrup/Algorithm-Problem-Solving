from math import gcd

def print_divisor(a):
    answer = []
    answer.append(a)
    for i in range(2, int(a**(1/2) + 1)):
        if a % i == 0:
            answer.append(i)
            if (i**2) != a:
                answer.append(a // i)
    answer.sort()
    print(*answer)

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)


result = []
for i in range(1, n):
    result.append(abs(arr[i]-arr[i-1]))

divisor = gcd(*result)
print_divisor(divisor)

