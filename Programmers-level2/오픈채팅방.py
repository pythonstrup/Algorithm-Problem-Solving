# 내풀이
# def solution(record):
#     dict_id = {}
#     dict_seq = {}
#     answer = []
#
#     for idx, sen in enumerate(record):
#         temp = sen.split()
#         if temp[0] == "Enter":
#             dict_id[temp[1]] = temp[2]
#             dict_seq[idx] = temp[1] + "님이 들어왔습니다."
#             # answer.append(temp[1])
#         elif temp[0] == "Leave":
#             # answer.append(temp[1])
#             dict_seq[idx] = temp[1] + "님이 나갔습니다."
#         elif temp[0] == "Change":
#             dict_id[temp[1]] = temp[2]
#
#     for idx, value in dict_seq.items():
#         answer.append(dict_id[value.split("님")[0]] + "님" + value.split("님")[1])
#
#     return answer

# 다른 사람 풀이
def solution(record):
    answer = []
    namespace = {}
    printer = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    for r in record:
        rr = r.split(" ")
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

r = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(r))