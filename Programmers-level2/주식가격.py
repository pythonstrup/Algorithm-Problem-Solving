# 내 풀이 - 효율성 테스트 17.05ms ~ 31.84ms
# 내 풀이가 웬만한 다른 풀이들보다 효율적임.
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for idx, price in enumerate(prices):

        while stack:
            if stack[-1][1] <= price:
                break
            i, p = stack.pop()
            answer[i] += idx-i

        stack.append((idx, price))

    while stack:
        i, p = stack.pop()
        answer[i] = idx-i

    return answer

# 나중에 다시 풀어본 내 풀이
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            temp = stack.pop()
            answer[temp[0]] = i - temp[0]

        stack.append((i, price))

    while stack:
        temp = stack.pop()
        answer[temp[0]] = n - temp[0] - 1

    return answer


# 다른 사람 풀이 - 효율성 테스트 92.32ms ~ 195.17ms
# 제일 간단한 풀이
# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
#     return answer

# 다른사람 풀이2 - 효율성 테스트 21.84ms ~ 39.32ms
# def solution(prices):
#     stack = []
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         if stack != []:
#             while stack != [] and stack[-1][1] > prices[i]:
#                 past, _ = stack.pop()
#                 answer[past] = i - past
#         stack.append([i, prices[i]])
#     for i, s in stack:
#         answer[i] = len(prices) - 1 - i
#     return answer

print(solution([1, 2, 3, 2, 3]))