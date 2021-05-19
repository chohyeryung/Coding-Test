def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()


participant1 = ["leo", "kiki", "eden"]
completion1 = ["eden", "kiki"]
print(solution(participant1, completion1))

participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion2 = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant2, completion2))

participant3 = ["mislav", "stanko", "mislav", "ana"]
completion3 = ["stanko", "ana", "mislav"]
print(solution(participant3, completion3))
