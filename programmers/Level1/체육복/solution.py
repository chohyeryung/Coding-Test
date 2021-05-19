def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for l in _lost:
        if l-1 in _reserve:
            _reserve.remove(l-1)
        elif l+1 in _reserve:
            _reserve.remove(l+1)
        else:
            n-=1
    return n

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve))