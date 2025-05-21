def solution(array, commands):
    result = []
    for i,j,k in commands:
        a = array[i-1:j]
        b = sorted(a)
        c = b[k-1]
        result.append(c)
    return result