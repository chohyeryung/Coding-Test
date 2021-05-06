def solution(n, lost, reserve):
    answer = n-len(lost)

    for i in range(len(reserve)):
        if(reserve[i]-1>0):
            reserve[i] = reserve[i] - 1

    for l in lost:
        if l in reserve:
            answer+=1
            reserve.remove(l)

    if answer != n-len(lost):
        for i in range(len(reserve)):
            reserve[i] = reserve[i] + 2

        for l in lost:
            if l in reserve:
                answer += 1

    return answer

n = 3
lost = [3]
reserve = [1]
print(solution(n, lost, reserve))