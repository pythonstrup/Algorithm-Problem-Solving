
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    # 중복 제거
    result = set(report)
    result = list(result)

    # [신고된 사람] : [신고한 사람]
    dict = {}
    for id in id_list:
        dict[id] = []

    # 신고한 유저와 유저가 신고한 아이디 나누기
    for i in result:
        show = i.split(" ")
        dict[show[1]] += [show[0]]


    # k명 이상 신고된 사람 찾기
    for key, value in dict.items():
        if len(value) >= k:
            for person in value:
                answer[id_list.index(person)] += 1

    return answer


id = ["muzi", "frodo", "apeach", "neo"]
report1 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id, report1, k))
