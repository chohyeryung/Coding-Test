def solution(s):
    answer = s[(len(s)-1)//2 : (len(s)+2)//2]
    return answer

print(solution("abcde"))
print(solution("qwer"))