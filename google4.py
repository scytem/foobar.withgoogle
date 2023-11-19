def solution(l):
    res = 0
    temp = [0] * len(l)
    for i in range(len(l) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if l[i] % l[j] == 0:
                temp[j] += 1
                res += temp[i]
    return res