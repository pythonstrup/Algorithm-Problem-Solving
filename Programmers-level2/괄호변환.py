# 내 풀이
def check_paren(s):
    stack = []
    for paren in s:
        if paren == '(':
            stack.append(paren)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return False if stack else True

def solution(p):
    if check_paren(p):
        return p

    open = 1 if p[0] == "(" else 0
    close = 1 if p[0] == ")" else 0
    for i in range(1, len(p)):
        if open == close:
            break
        else:
            if p[i] == "(": open += 1
            else: close += 1
    u = "".join(p[:open+close])
    v = "".join(p[open+close:])

    answer = ""
    if not check_paren(u):
        answer = "(" + solution(v) + ")"
        for i in range(1, len(u)-1):
            answer += "(" if u[i] == ")" else ")"
    else: answer = u + solution(v)

    return answer


# 다른 사람 풀이 1
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))

# 다른 사람 풀이 2
def divide(p):
    open_p = 0
    close_p = 0

    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1

        if open_p == close_p:
            return p[:i + 1], p[i + 1:]

def check(u):
    stack = []

    for p in u:
        if p == "(":
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()

    return True

def solution(p):
    if not p:
        return ""

    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

        return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
print(solution(""))
print(solution("))))(((("))
print(solution("))(()("))
print(solution(")()()()("))
