def solution(numbers, hand):
    answer = ''
    left = (3, 0)
    right = (3, 2)
    key = [ (3,1), (0,0), (0, 1), (0,2), (1,0), (1, 1), (1,2), (2,0), (2, 1), (2,2), (3,0), (3,2) ]

    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left = key[number]
        elif number in [3, 6, 9]:
            answer += "R"
            right = key[number]
        else:
            distance_l = abs(key[number][0] - left[0]) + abs(key[number][1] - left[1])
            distance_r = abs(key[number][0] - right[0]) + abs(key[number][1] - right[1])
            if distance_r < distance_l:
                answer += "R"
                right = key[number]
            elif distance_r > distance_l:
                answer += "L"
                left = key[number]
            else:
                if hand == "right":
                    answer += "R"
                    right = key[number]
                else:
                    answer += "L"
                    left = key[number]

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
print(solution(numbers, "right"))


