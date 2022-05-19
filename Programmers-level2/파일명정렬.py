# 내 풀이 - 최대 2ms
def solution(files):
    result = []

    for file in files:
        is_number = False
        head = ""
        number = ""
        tail = ""
        for i, c in enumerate(file):
            if c.isdigit():
                is_number = True
                number += c
            else:
                if is_number:
                    tail = file[i:]
                    break
                else:
                    head += c
        result.append([head, number, tail])

    result.sort(key=lambda x: int(x[1]))
    result.sort(key=lambda x: x[0].upper())

    answer = ["".join(x) for x in result]
    return answer

# 다른 사람 풀이 - 4ms
# 성능 자체는 내 풀이가 좋지만....
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))