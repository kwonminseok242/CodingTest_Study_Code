def solution(array):
    
    a = []
    for i in array:
        if a[-1:] == [i]: continue
        a.append(i)
    return a