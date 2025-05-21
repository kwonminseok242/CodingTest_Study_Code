def solution(s):
    answer = s.split(" ",-1) #['try', 'hello', 'world']
    b = ""
    c = []
    for i in answer: #['try', 'hello', 'world']
        b = ""
        for j in range(len(i)):
            if j % 2 == 0:
                b += i[j].upper()
            else :
                b += i[j].lower()
        c.append(b)
    print(c)
    

    return ' '.join(c)