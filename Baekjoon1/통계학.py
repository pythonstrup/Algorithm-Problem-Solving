from collections import Counter

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

array.sort()

cnt = Counter(array)
value = cnt.most_common()
value.sort(key=lambda x:x[1], reverse=True)

if n > 1:
    if value[0][1] == value[1][1]:
        result = value[1][0]
    else:
        result = value[0][0]
else:
    result = value[0][0]



print(round(sum(array)/n))
print(array[n//2])
print(result)
print(array[n-1]-array[0])