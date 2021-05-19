def solution(n, m):
    gongyak = 0
    for i in range(1, m):
        if n%i==0 and m%i==0:
            gongyak = i
    gongbae = n*m // gongyak
    answer = []
    answer.append(gongyak)
    answer.append(gongbae)
    return answer

print(solution(3, 12))
print(solution(2, 5))