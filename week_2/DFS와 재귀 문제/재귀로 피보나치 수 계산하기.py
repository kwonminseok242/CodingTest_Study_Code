"""
[문제 4]
주어진 자연수 n 에 대해 n번재 피보나치 수를 재귀를 사용하여 계산하는 프로그램을 작성하세요.

[예시]
fibonacci(5) → 5
fibonacci(6) → 8

힌트: 피보나치 수는 fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)이며, 
종료 조건은 fibonacci(0) = 0, fibonacci(1) = 1입니다.
"""

# def fibonacci(n):
#     if fibonacci(0) == 0:
#         return 0
#     elif fibonacci(1) == 1:
#         return 1
#     elif n <= 0:
#         print("음수에는 피보나치 수열이 정의되지 않습니다.")
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
"""
[feedback]
피보나치 수열의 종료 조건을 fibonacci(0) == 0과 fibonacci(1) == 1로 확인하고 있습니다. 
이 부분은 잘못된 조건입니다. fibonacci(0)과 fibonacci(1)을 호출하는 것이 아니라, 
함수 내에서 직접 비교해야 합니다.
올바른 종료 조건은 n == 0 또는 n == 1입니다.

n <= 0에서 음수를 처리하려는 의도는 좋습니다. 
하지만 print문만 출력하고 함수가 종료되지 않기 때문에 불완전한 처리입니다. 
ValueError 예외를 발생시키는 방식으로 처리하면 좋습니다.

def fibonacci(n):
    # 음수일 경우 예외 처리
    if n < 0:
        raise ValueError("음수에는 피보나치 수열이 정의되지 않습니다.")
    # 종료 조건: n이 0이면 0 반환, n이 1이면 1 반환
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    # 재귀적으로 피보나치 계산
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

"""

def fibonacci(n):
    # 음수일 경우 예외 처리
    if n < 0:
        raise ValueError("음수에는 피보나치 수열이 정의되지 않습니다.")
    # 종료 조건: n이 0이면 0 반환, n이 1이면 1 반환
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    # 재귀적으로 피보나치 계산
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(0))