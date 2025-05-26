# 문제1
# 주어진 무방향 그래프에서 연결된 컴포넌트의 개수를 구하는 프로그램을 작성하세요.
"""
[그래프 예시]
    0 - 1 - 2
    |
    4
    |
    3

    5            

출력 예시 : 연결된 컴포넌트의 수 = 2

힌트1 : DFS를 사용하여 그래프를 탐색하고, 아직 방문하지 않은 노드를 만나면 그 노드를 
        시작으로 DFS를 실행하여 하나의 연결된 컴포넌트를 찾습니다.
힌트2 : 그래프를 인접 리스트 형식으로 표현해보자
힌트3 : 방문 처리
graph = {
    0 : [1,2,3,4],
    1 : [0,2],
    2 : [0,1],
    3 : [0,4],
    4 : [0,3],
    5 : []
==> 틀린 그래프 이 그래프는 0이 모든 노드와 직접 연결되어있다는 것을 뜻하는 형태
}
"""
graph = {
    0 : [1,4],     # 0은 1, 4와 연결
    1 : [0,2],     # 1은 0, 2와 연결
    2 : [1],       # 2는 1과 연결
    3 : [4],       # 3은 4와 연결
    4 : [0,3],     # 4는 0, 3과 연결
    5 : []         # 5는 독립적
}

def dfs(graph,node,visited):
    visited.add(node) # 현재 노드를 방문 표시 (노드를 vistited라는 리스트에 넣어줌)
    for neighbor in graph[node]:
        if neighbor not in visited: # 방문리스트에 노드 번호가 없으면
            dfs(graph, neighbor, visited) # 그 노드 방문하러가기 재귀

def count_components(graph):
    visited = set()
    component_count = 0
    
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
            component_count += 1
    return component_count

print("연결된 컴포넌트의 수:", count_components(graph))

for node in graph:
    print(node)






