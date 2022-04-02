def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    content = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    day = sum(days[:a-1]) + b
    for i in range(7):
        if day % 7 == i:
            answer = content[i]
    return answer

print(solution(5, 24))