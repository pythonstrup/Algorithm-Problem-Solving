
s = input().split("-")
result = 0
for i in s[0].split("+"):
    result += int(i)
for i in s[1:]:
    for j in i.split("+"):
        result -= int(j)

print(result)


# 내 풀이
# form = input()
# numbers = []
# operator = []
#
# start = 0
# for i in range(len(form)):
#     if form[i] == "-" or form[i] == "+":
#         operator.append(form[i])
#         numbers.append(int(form[start:i]))
#         start = i+1
# numbers.append(int(form[start:]))
#
# result = numbers[0]
# for i in range(len(operator)):
#     if operator[i] == "-":
#         result -= sum(numbers[i+1:])
#         break
#     result += numbers[i+1]
#
# print(result)

