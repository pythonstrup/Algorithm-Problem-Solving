# 효율성테스트 통과 실패
def solution(info, query):
    answer = []
    user = []
    word = ["language", "field", "spot", "soul_food", "score"]

    for i in info:
        temp_dict = {}
        for index, s in enumerate(i.split()):
            temp_dict[word[index]] = s

        user.append(temp_dict)

    for q in query:
        result = 0
        for u in user:
            is_same = True
            index = 0
            for str in q.split():
                if str == "and":
                    continue

                if str.isdigit():
                    if int(str) <= int(u[word[index]]):
                        print(str, u[word[index]])
                        break
                    else:
                        is_same = False
                        break

                if str == "-":
                    index += 1
                    continue

                if u[word[index]] == str:
                    index += 1
                else:
                    is_same = False
                    break
            if is_same: result += 1
        answer.append(result)

    return answer

print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]))