def solution(phone_number):
    k = list(phone_number)
    a = k[-1:-5:-1]
    b = len(a)
    c = len(phone_number)
    d = c-b
    e = "*"*d
    answer = f'{e}{a[3]}{a[2]}{a[1]}{a[0]}'
    return answer