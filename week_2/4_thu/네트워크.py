def dfs(i, visited, computers, n):
    visited[i] = "지나감"
    for next in range(n):
        if visited[next] == "안지나감" and computers[i][next] == 1:
            dfs(next, visited, computers, n)

def solution(n, computers):
    answer = 0
    visited = ["안지나감"] * n
    for i in range(n):
        if visited[i] == "안지나감":
            dfs(i, visited, computers, n)
            answer += 1
    return answer

n = 3
computers = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

print(solution(n, computers))