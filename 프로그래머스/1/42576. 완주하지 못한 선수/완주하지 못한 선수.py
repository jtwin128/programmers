def solution(participant, completion):
    answer = ''
    participants = {}
    
    for i in participant:
        if i in participants:
            participants[i] +=1
        else:
            participants[i] = 1
            
    for i in completion:
        if i in participants:
            participants[i] -=1

    for key, value in participants.items():
        if value != 0:
            answer = key
 
    
    return answer