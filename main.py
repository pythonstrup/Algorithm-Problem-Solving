from collections import Counter

def duplicated(arr):
    count = Counter(arr)
    answer = []
    for key, value in count.items():
        if value > 1:
            answer.append(value)

    return answer if answer else [-1]


print(duplicated([1,2,3,3,3,3,4,4]))
print(duplicated([3,5,7,9,1]))
print(duplicated([3,2,4,4,2,5,2,5,5]))