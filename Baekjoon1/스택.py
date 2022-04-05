
n = int(input())
operation = []
for i in range(n):
    operation.append(input().split())

stack = []
for i in operation:
    if i[0] == "push":
        stack.append(int(i[1]))

    elif i[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif i[0] == "size":
        print(len(stack))

    elif i[0] == "empty":
        print(1 if len(stack) == 0 else 0)

    elif i[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

