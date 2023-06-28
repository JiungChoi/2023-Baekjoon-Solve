# 트리의 부모찾기 : DFS, 스택
from sys import stdin

N = int(stdin.readline())
graph = [[] for _ in range(N + 1)]
haveParent = [False] * (N+1)

def whoIsParent(graph):
    
    queue = [1]
    while queue:
        nowVertex = queue.pop()
        for nextVertex in graph[nowVertex]:
            if not haveParent[nextVertex]:
                haveParent[nextVertex] = nowVertex
                queue.append(nextVertex)
 

for i in range(1, N):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

whoIsParent(graph)
print("\n".join(map(str, haveParent[2:])))