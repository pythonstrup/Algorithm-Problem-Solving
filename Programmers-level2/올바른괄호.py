# 내 풀이
# 나름 정석이라고 생각됨
def solution(s):
    stack = []
    for paren in s:
        if paren == '(':
            stack.append(paren)
        else:
            if stack:
                stack.pop()
            else:
                return False
    # return len(stack) == 0
    # return False if stack else True
    if stack:
        return False
    else:
        return True


# 다른 사람 풀이1
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)
        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False
    return len(st) == 0


# 다른 사람 풀이2
def is_pair(s):
    # 함수를 완성하세요
    open_cnt = 0
    for c in s:
        if c == '(':
            open_cnt += 1
        elif c == ')':
            open_cnt -= 1
            if open_cnt < 0:
                return False
    return open_cnt == 0

print(solution("()()"))
print(solution("(())()"	))
print(solution(")()("	))
print(solution("(()("	))


