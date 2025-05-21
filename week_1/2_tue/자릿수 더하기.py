def solution(n):
    a = str(n)

    llist = list(a)
    fuck = len(llist)
    total = 0

    for i in range(fuck):
        a = int(llist[i])
        total += a

    return total