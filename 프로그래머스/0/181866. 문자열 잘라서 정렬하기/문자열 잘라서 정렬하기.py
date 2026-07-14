def solution(myString):
    answer = []
    
    start = 0
    pos = myString.find("x")
 
    while pos != -1:
        word = myString[start:pos]
        if word:
            answer.append(word)

        start = pos + 1
        pos = myString.find("x", start)

    word = myString[start:]
    if word:
        answer.append(word)
        
    answer.sort()
    return answer