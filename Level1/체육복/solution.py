def solution(n, lost, reserve):
    answer = 0
    for r in reserve:
        for l in lost:
            if r+1 == l or r-1 == l:
                answer+=1
    return answer

n = 5
lost = [2, 4]
reserve = [3]
print(solution(n, lost, reserve))