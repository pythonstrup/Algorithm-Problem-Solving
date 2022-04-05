

n = int(input())
words = []
for _ in range(n):
    words.append(input())

words = list(set(words))
words.sort(key=lambda x: (len(x), x))
for i in words:
    print(i)