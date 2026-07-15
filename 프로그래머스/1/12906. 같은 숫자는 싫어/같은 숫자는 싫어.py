def solution(arr):
    answer = []
    number = arr[0]
    answer.append(number)
    
    for idx in range(1, len(arr)):
        if number != arr[idx]:
            number = arr[idx]
            answer.append(number)
            
    return answer