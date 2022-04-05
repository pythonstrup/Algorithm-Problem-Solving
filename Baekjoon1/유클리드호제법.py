# 유클리드 호제법
# 입력으로 두 수 a, b(a > b)이 들어온다.
# b이 0이라면, a를 출력하고 알고리즘을 종료한다.
# a이 b으로 나누어 떨어지면, b을 출력하고 알고리즘을 종료한다.
# 그렇지 않으면, a를 b으로 나눈 나머지를 새롭게 b에 대입하고, a에 b를 대입하고(동시에) 3번으로 돌아온다.
def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a


x, y = map(int, input().split())

result = gcd(x, y)
print(result)
# 최소공배수 = 변수1 * 변수2 / 최대공약수
print(x * y // result)