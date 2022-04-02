# def solution(arr, divisor):
#     arr = list(filter(lambda x: x % divisor == 0, arr))
#     if len(arr) == 0:
#         return [-1]
#
#     return sorted(arr)



def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]