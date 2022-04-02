
def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0] * 3

    for i in range(len(answers)):
        if person1[i % len(person1)] == answers[i]:
            scores[0] += 1
        if person2[i % len(person2)] == answers[i]:
            scores[1] += 1
        if person3[i % len(person3)] == answers[i]:
            scores[2] += 1

    answer = []
    for i, score in enumerate(scores):
        if score == max(scores):
            answer.append(i+1)

    return answer


answer1 = [1,2,3,4,5]
answer2 = [1,3,2,4,2]
answer3 = [2, 1, 1, 3, 2]

print(solution(answer1))
print(solution(answer2))
print(solution(answer3))