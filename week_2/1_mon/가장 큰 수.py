def solution(numbers):
    # 숫자들을 문자열로 변환
    numbers = list(map(str, numbers))

    # 정렬: 'x*3'을 키로 사용 (최대 길이를 고려한 반복)
    # 내림차순 정렬(reverse=True)
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # 정렬된 숫자들을 이어붙임
    result = ''.join(numbers)

    # '0000...' -> '0' 처리
    return str(int(result))