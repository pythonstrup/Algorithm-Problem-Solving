from itertools import permutations

def operation(num1, num2, op):
    if op == "+":
        return str(int(num1) + int(num2))
    elif op == "-":
        return str(int(num1) - int(num2))
    elif op == "*":
        return str(int(num1) * int(num2))

def calculate(exp, op):
    array = []
    tmp = ""
    for i in exp:
        if i.isdigit():
            tmp += i
        else:
            array.append(tmp)
            array.append(i)
            tmp = ""
    array.append(tmp)

    for s in op:
        stack = []
        while len(array) != 0:
            tmp = array.pop(0)
            if tmp == s:
                stack.append(operation(stack.pop(), array.pop(0), s))
            else:
                stack.append(tmp)
        array = stack

    return abs(int(array[0]))

def solution(expression):
    op = ["+", "-", "*"]
    op = list(permutations(op, 3))
    result = []
    for i in op:
        result.append(calculate(expression, i))
    return max(result)

print(solution("100-200*300-500+20"))