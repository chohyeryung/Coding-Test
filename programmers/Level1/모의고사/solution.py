def solution(answer):
    an=[]
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    grade = [0,0,0]
    for i in range(len(answer)):
        if answer[i] == first[i%len(first)]:
            grade[0]+=1
        if answer[i] == second[i%len(second)]:
            grade[1]+=1
        if answer[i] == third[i%len(third)]:
            grade[2]+=1

    for person,score in enumerate(grade):
        if score==max(grade):
            an.append(person+1)
    return an

answers = [1,3,2,4,2]
print(solution(answers))