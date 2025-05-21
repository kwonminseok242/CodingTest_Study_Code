def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[0] == arr[-1]:
            if arr[i] != arr[i-1] or arr[i-2] == 0:
                answer.append(arr[i-1])
        elif arr[0] != arr[-1]:
            if arr[i] != arr[i-1]:
                answer.append(arr[i])
    return answer