def solution(n, lost, reserve):
    answer = n-len(lost)

    for i in range(len(reserve)):
        reserve[i] = reserve[i]-1

    for l in lost:
        if l in reserve:
            answer+=1

    for i in range(len(reserve)):
        reserve[i] = reserve[i] + 1

    for l in lost:
        if l in reserve:
            answer += 1

    return answer

n = 5
lost = [2, 4]
reserve = [3]
print(solution(n, lost, reserve))