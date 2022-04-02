def solution(n, lost, reserve):
    reserve_pro = list(set(reserve) - set(lost))
    lost_pro = list(set(lost) - set(reserve))

    for i in reserve_pro:
        if i-1 in lost_pro:
            lost_pro.remove(i-1)
        elif i+1 in lost_pro:
            lost_pro.remove(i+1)

    answer = n - len(lost_pro)
    return answer


n1 = 5
lost1 = [2, 4]
reserve1 = [1, 3, 5]
n2 = 5
lost2 = [2, 4]
reserve2 = [3]
n3 = 15
lost3 = [3, 4, 6, 8, 9, 11]
reserve3 = [1, 2, 7, 10]

print(solution(n1, lost1, reserve1))
print(solution(n2, lost2, reserve2))
print(solution(n3, lost3, reserve3))

