def solution(s):
    if s[0] == "+":
        return int(s[1:])
    elif s[0] == "-":
        return -int(s[1:])
    else:
        return int(s)


print(solution("+1234"))


arr = [1,2,3,4,5,6]
print(arr[::-1])
print(arr[::-2])
print(arr[::2])