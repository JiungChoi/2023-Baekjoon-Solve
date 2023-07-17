'''
    제목 : DFS와 BFS
    문제 : 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
    입력 : 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

    풀이 :
        DFS : 스택
        BFS : 큐
        그래프를 그리고 그래프의 원본 데이터를 수정하지 않도록 함수를 사용한다.
        재귀함수를 사용하지 않고 구현, 방문 정점이 여러개인 경우 작은 수부터 방문이므로 정렬을 먼저한다.
'''

from sys import stdin

N, M, V = map(int, stdin.readline().split())

def dfs(grp, v):
    
    stack = [v]
    visited = [False for _ in range(N+1)]

    # Sort
    for i in range(N+1):
        graph[i].sort(reverse=True)

    ary = []
    while stack:
        now = stack.pop()
        if visited[now] == False:
            visited[now] = True
            stack += grp[now]
            ary.append(now)
    return ary

def bfs(grp, v):
    
    queue = [v]
    visited = [False for _ in range(N+1)]

    # Sort
    for i in range(N+1):
        graph[i].sort()

    ary = []
    while queue:
        now = queue[0]
        queue = queue[1:]
        if visited[now] == False:
            visited[now] = True
            queue += grp[now]
            ary.append(now)
    return ary

# Input Graph
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

print(*dfs(graph, V))
print(*bfs(graph, V))