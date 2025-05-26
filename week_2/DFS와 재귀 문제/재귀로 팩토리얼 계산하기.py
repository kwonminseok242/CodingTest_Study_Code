# 문제 2
# 주어진 자연수 n에 대해 n! (팩토리얼)을 계산하는 재귀 함수 factorial(n)을 작성하세요.
# 힌트: 팩토리얼은 재귀적으로 구할 수 있습니다. n! = n * (n - 1)!이고, 종료 조건은 0! = 1입니다.

# def factorial(n):
#     if n == 0:
#         print("종료")
#         return 1
#     else:
#         print(n*factorial(n-1))
#         return n*factorial(n-1)
    
def factorial(n):
    if n == 0:
        print("종료")
        return 1
    else:
        result = n * factorial(n - 1)
        print(result)
        return result

# 함수 호출
factorial(3)
# 3 * factorial(2) => 3 * 2 * factorial(1) => 3 * 2 * 1 * factorial(0) => 3 * 2 * 1 * 1 = 6
#     factorial(2) = 2*factorial(1)
#                      factorial(1) = 1*factorial(0)
#                                       factorial(0) = 1
    
"""
[feedback]
n이 음수일 경우에 대한 처리가 필요할 수 있습니다. 
음수에 대해서는 팩토리얼이 정의되지 않으므로, 
이 경우에 예외를 처리하는 것이 좋습니다.

def factorial(n):
    if n < 0:
        raise ValueError("음수에는 팩토리얼이 정의되지 않습니다.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
"""