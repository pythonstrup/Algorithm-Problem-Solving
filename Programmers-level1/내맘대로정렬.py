def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])


print(solution(["abce", "abcd", "cdx", "axbd"], 2))
print(solution(["abce", "abcd", "cdx", "axbd"], 1))
print(solution(["abce", "abcd", "cdx", "axbd"], 0))