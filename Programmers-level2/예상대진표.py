# 내 풀이
def solution1(n,a,b):
    import math
    answer = 0

    for i in range(int(math.log2(n))):
        if a == b: break

        # if-else문 필요없이 그냥 (a+1)//2 했으면 됨.
        if a % 2 == 0: a //= 2
        else: a = (a+1)//2

        if b % 2 == 0: b //= 2
        else: b = (b+1)//2

        answer += 1

    return answer

# 내 풀이 조금 수정
def solution(n,a,b):
    import math
    answer = 0

    # 로그2로 돌리는 for문 대신 while 써도됨.
    for i in range(int(math.log2(n))):
        # a와 b 둘이 붙으면 둘 중 한명만 올라가기 때문에 수가 똑같아짐
        if a == b: break

        a = (a+1)//2
        b = (b+1)//2
        answer += 1

    return answer

# 다른 사람 풀이
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()


print(solution(8,4,7))
print(solution(32,8,10))