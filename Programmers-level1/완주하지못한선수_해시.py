def solution(participant, completion):
    answer = ''
    dict = {}
    summary = 0
    for person in participant:
        dict[hash(person)] = person
        summary += hash(person)

    for person in completion:
        summary -= hash(person)

    answer = dict[summary]
    return answer

participant1 = ["leo", "kiki", "eden"]
completion1 = ["eden", "kiki"]
print(solution(participant1, completion1))