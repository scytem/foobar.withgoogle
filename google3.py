def solution(s):
    res = 0
    right = []
    left = []
    loc = 0
    for char in s:
        if char == ">":
            right.append(loc)
        if char == "<":
            left.append(loc)
        loc += 1
    for i in range(len(right)):
        for j in range(len(left)):
            if right[i] < left[j]:
                res += 2
    return res

print(solution("--->-><-><-->-"))

