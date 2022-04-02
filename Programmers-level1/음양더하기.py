def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

absol1 = [4, 7 ,12]
sign1 = [True, False, True]
absol2 = [1, 2, 3]
sign2 = [False, False, True]

print(solution(absol1, sign1))
print(solution(absol2, sign2))