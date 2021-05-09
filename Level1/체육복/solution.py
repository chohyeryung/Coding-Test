def solution(n, lost, reserve):
    answer = n-len(lost)
    for l in lost:
        if l-1 in reserve:
            answer+=1
            reserve.remove(l-1)
        elif l+1 in reserve:
            answer+=1
            reserve.remove(l-1)
    return answer

n = 3
lost = [3]
reserve = [1]
print(solution(n, lost, reserve))