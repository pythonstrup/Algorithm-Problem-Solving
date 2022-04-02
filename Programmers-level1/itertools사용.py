import itertools

def solution(numbers):
    result = list(itertools.combinations(numbers, 2))
    answer = []
    for i in result:
        if not sum(i) in answer:
            answer.append(sum(i))

    answer.sort()
    return answer

num = [2,1,3,4,1]
result = list(itertools.permutations(num, 2))
print(result)
print(solution(num))