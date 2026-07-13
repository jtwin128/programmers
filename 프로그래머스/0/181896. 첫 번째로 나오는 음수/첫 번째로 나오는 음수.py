def solution(num_list):
    count = 0
    answer = 0
    
    for i in range(len(num_list)):
        if num_list[i] < 0:
            count+=1
            index = i
            break
            
    if count > 0:
        answer = index
    else:
        answer = -1
        
    return answer