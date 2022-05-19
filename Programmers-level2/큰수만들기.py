# 내 풀이
def solution(number, k):
    save = []
    for i in number:
        while save and k != 0 and save[-1] < i:
            save.pop()
            k -= 1
        save.append(i)

    # 테스트 케이스 12번 통과하려면
    while k:
        save.pop()
        k -= 1

    return "".join(save)


# 다른 사람 풀이 1
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


# 다른 사람 풀이 2
def solution(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    return ''.join(st[:len(st) - k])


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
