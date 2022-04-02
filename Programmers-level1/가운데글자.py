def solution(s):
    if len(s) % 2 == 1:
        return s[len(s)//2]
    else:
        return s[len(s)//2 - 1]+s[len(s)//2]


#모범답안
def string_middle(str):
    # 함수를 완성하세요
    return str[(len(str)-1)//2:len(str)//2+1]

print(solution("qwer"))
print(solution("qwerq"))
