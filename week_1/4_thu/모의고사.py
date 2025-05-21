def solution(a):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2]
    a3 = [3, 3, 1, 1, 2]
    a1_score = 0
    a2_score = 0
    a3_score = 0
    list1 = []
    for i in range(5):
        if a1[i] == a[i]:
            a1_score += 1
        if a2[i] == a[i]:
            a2_score += 1
        if a3[i] == a[i]:
            a3_score += 1
    score_index = [a1_score,a2_score,a3_score]
    answer =[]
    for i in range(3):
        if score_index[i] == max(score_index):
            answer.append(i + 1) 

    return answer

a = [1,2,3,4,5]
print(solution(a))
print(solution([1,3,2,4,2]))