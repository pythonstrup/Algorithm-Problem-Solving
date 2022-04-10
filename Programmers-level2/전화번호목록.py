# 가장 간단한 풀이
# 효율성테스트를 못넘음 ㅠㅜ
# def solution(phone_book):
#
#     for number in phone_book:
#         for j in phone_book:
#             if number == j:
#                 continue
#             elif number.startswith(j):
#                 return False
#     return True

# 정렬을 이용한 풀이
# 반복문이라 그런지 효율성테스트를 통과못함
# def solution(phone_book):
#     phone_book.sort()
#     n = len(phone_book)
#
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if phone_book[j].startswith(phone_book[i]):
#                 return False
#     return True

# def solution(phone_book):
#     phone_book.sort()
#     n = len(phone_book)
#
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 return False
#     return True

# 해쉬 사용
def solution(phone_book):
    dic = {i: 1 for i in phone_book}
    for number in phone_book:
        tmp = ""
        for i in number:
            tmp += i
            if tmp in dic and tmp != number:
                return False
    return True



print(solution(["119", "97674223", "1195524421"]))
print(solution(["12","123","1235","567","88"]))
print(solution(["123","456","789"]))