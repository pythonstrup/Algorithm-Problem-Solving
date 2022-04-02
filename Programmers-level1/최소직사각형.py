# def solution(sizes):
#     width = max(sizes, key=lambda x: x[0])
#     height = max(sizes, key=lambda x: x[1])
#     line1 = max(width[0], height[1])
#     line2 = 0
#     for i in sizes:
#         if line2 < min(i):
#             line2 = min(i)
#     return line1 * line2


def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

size = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(size))