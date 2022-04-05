
n = int(input())
pos = list(map(int, input().split()))
zipped = sorted(list(set(pos)))

dic = {zipped[i] : i for i in range(len(zipped))}

for i in pos:
    print(dic[i], end=" ")
