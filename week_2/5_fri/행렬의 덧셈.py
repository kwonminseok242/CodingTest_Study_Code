def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)): # 0 1
        d = []
        for j in range(len(arr1[i])): 
            d.append(arr1[i][j]+arr2[i][j])
        answer.append(d)

    return answer