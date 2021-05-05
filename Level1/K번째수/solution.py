def solution(array, commands):
    i=0
    j=0
    k=0
    for command in commands:
        i = command[0]
        j = command[1]
        array = array[i-1:j]
        print(array)
        k = command[2]



array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
