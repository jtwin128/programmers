def solution(s):

    stack = []
    a = list(s)
    
    for i in a:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    
    if not stack:
        return True
    else:
        return False