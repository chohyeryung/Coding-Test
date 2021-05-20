def solution(s):
    answer = True
    s = s.lower()
    p = s.count('p')
    y = s.count('y')
    if p==y:
        answer = True
    else:
        answer = False

    return answer

print(solution("pPoooyY"))
print(solution("Pyy"))