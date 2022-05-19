# 내 풀이
# 다음에 풀이할 때는 함수화를 하자
def solution(fees, records):
    import math

    info = []
    car_fee = {}
    for record in records:
        temp = record.split(" ")
        car_fee[temp[1]] = 0

        # 시간을 분 단위로 다 바꿔줌
        time = temp[0].split(":")
        temp[0] = int(time[0])*60 + int(time[1])
        info.append(temp)

    parking = {}
    for i in info:
        if i[2] == 'IN':
            parking[i[1]] = i[0]
        else:
            m = i[0] - parking[i[1]]
            car_fee[i[1]] += m
            parking.pop(i[1])

    last_time = 23*60 + 59
    for key, value in parking.items():
        car_fee[key] += last_time - value

    print(car_fee)
    answer = []
    for key, m in car_fee.items():
        if m <= fees[0]:
            answer.append([key, fees[1]])
        else:
            answer.append([key, fees[1] + math.ceil((m-fees[0]) / fees[2]) * fees[3]])

    return [x[1] for x in sorted(answer)]

# 다른 사람 풀이
from collections import defaultdict
from math import ceil

class Parking:
    def __init__(self, fees):
        self.fees = fees
        self.in_flag = False
        self.in_time = 0
        self.total = 0

    def update(self, t, inout):
        self.in_flag = True if inout=='IN' else False
        if self.in_flag:  self.in_time = str2int(t)
        else:             self.total  += (str2int(t)-self.in_time)

    def calc_fee(self):
        if self.in_flag: self.update('23:59', 'out')
        add_t = self.total - self.fees[0]
        return self.fees[1] + ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1]

def str2int(string):
    return int(string[:2])*60 + int(string[3:])

def solution(fees, records):
    recordsDict = defaultdict(lambda:Parking(fees))
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout)
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]

# 다른 사람 풀이 2
import math

def changeToMinute(first, second):
    h1, m1 = map(int, first.split(':'))
    h2, m2 = map(int, second.split(':'))
    total1, total2 = h1 * 60 + m1, h2 * 60 + m2

    return total2 - total1;

def solution(fees, records):
    dt, df, ut, uf = fees
    check = {}
    check_time = {}

    # in-out 둘다 있는 차량 주차시간 구하기
    for record in records:
        when, car, inout = record.split()
        if inout == "IN":
            check[car] = when
        else:
            if car not in check_time:
                check_time[car] = changeToMinute(check[car], when)
            else:
                check_time[car] += changeToMinute(check[car], when)
            check[car] = "0"

    # 23:59에 출차된 것으로 간주할 때 주차시간 구하기
    for key, value in check.items():
        if value != "0":
            if key in check_time:
                check_time[key] += changeToMinute(value, "23:59")
            else:
                check_time[key] = changeToMinute(value, "23:59")  # 테스트3번에서 check_time에 아예 아무것도 안들어가있을 수도 있음

    check_time = sorted(check_time.items())

    answer = []
    for car, total_time in check_time:
        if total_time <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((total_time - dt) / ut) * uf)

    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
                "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))

print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))