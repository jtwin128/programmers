def solution(array, commands):
    answer = []
    for command in commands:
        a = []
        i, j, k = command
        a = array[i-1:j]
        a.sort()
        b = a[k-1]
        answer.append(b)
    return answer