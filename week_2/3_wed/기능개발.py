def solution(progresses, speeds):
    answer = []
    date = []
    score = 0
    #ff
    for i in range(len(progresses)):
        a = (100-progresses[i])%speeds[i]
        b = (100-progresses[i])//speeds[i]
        if a == 0:
            date.append(b)
        elif a > 0:
            date.append(b+1)
    standard = date[0]   
    for i in range(1,len(date)):
        if date[i] <= standard:
            score += 1
        else:
            standard = date[i]
            answer.append(score+1)
            score = 0
    answer.append(score+1)
    return answer