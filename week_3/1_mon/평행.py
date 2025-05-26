def solution(dots):
    d1 = dots[0]
    answer = [] 
    for i in range(1,4):
        a = dots[i]
        x = (a[0]-d1[0])/(a[1]-d1[1])
        if i == 1: # 0-1 = 2-3
            y = (dots[2][0]-dots[3][0])/(dots[2][1]-dots[3][1])
            # print("i가 = 1 일때",y)
            # print("0-1 값은 : ",x)
            if x == y:
                return 1

        elif i == 2: # 0-2 = 1=3
            y = (dots[1][0]-dots[3][0])/(dots[1][1]-dots[3][1])
            # print("i가 = 2 일때",y)
            # print("0-2 값은 : ",x)
            if x == y:
                return 1

        elif i == 3: # 0-3 = 1-2
            y = (dots[1][0]-dots[2][0])/(dots[1][1]-dots[2][1])
            # print("i가 = 3 일때",y)
            # print("0-3 값은 : ",x)
            if x == y:
                return 1
    return 0 