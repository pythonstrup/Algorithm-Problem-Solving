# 오류 발생
def solution(name):
    answer = 0
    cost = [min(ord(alp) - ord('A'), ord('Z') - ord(alp) + 1) for alp in name]
    idx = 0

    while True:
        answer += cost[idx]
        cost[idx] = 0
        if sum(cost) == 0:
            return answer

        left, right = 1, 1
        while cost[idx - left] == 0:
            left += 1
        while cost[idx + right] == 0:
            right += 1

        print(idx, left, right)
        answer += left if left < right else right
        idx += -left if left < right else right

    return answer

# 정답
def solution(name):
    # 조이스틱 조작 횟수
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer


n = "JEROEN"
print(solution(n))

n = "JAN"
print(solution(n))

n = "ABABAABA"
print(solution(n))

n = "AAAABABAAAA"
print(solution(n))