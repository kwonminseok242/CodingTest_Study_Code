def solution(s):
    total_P = 0
    total_Y = 0

    for i in str(s):
        if i == "p" or i == "P":
            total_P += 1
        elif i == "y" or i == "Y":
            total_Y += 1

    if total_Y == total_P:
        return True
    elif total_Y != total_P:
        return False
    else:
        return True
