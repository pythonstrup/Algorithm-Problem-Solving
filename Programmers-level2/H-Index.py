# 내풀이 - 테스트 11, 16밖에 통과 못함.
# def solution(citations):
#     answer = 0
#     n = len(citations)
#
#     citations.sort()
#     count = 0
#     for citation in citations:
#         if n - count >= citation and count <= citation:
#             answer = citation
#         count += 1
#
#     return answer

## 내가 틀린이유
# H-Index를 정확히 인지하지 못했다.

## 정답 문제 풀이
def solution(citations):
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx

    return 0