def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

""" 나와 비슷한 정답
def solution(citations):
    max_h = 0
    for h in range(0, max(citations) + 1):  # 가능한 모든 h값 시도
        count = 0
        for c in citations:
            if c >= h:
                count += 1
        if count >= h:
            max_h = h
    return max_h
"""