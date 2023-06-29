# 트리의 지름 : 너비기반 탐색 (BFS)
from sys import stdin
from collections import deque

INF = -1

def longest(start):
    queue = deque()
    queue.append([start, 0])
    distance[start] = 0
    visited[start] = True

    while queue:
        node, cost = queue.popleft()

        for next_node, next_cost in tree[node]:
            if not visited[next_node]:
                visited[next_node] = True
                next_cost += cost
                distance[next_node] = next_cost
                queue.append([next_node, next_cost])

    return distance

V = int(stdin.readline())
tree = [[] for _ in range(V+1)]

distance = [INF]*(V+1)

for _ in range(V):
    treeInfo = list(map(int, stdin.readline().split()))
    for i in range(1, len(treeInfo) - 2, 2):
        tree[treeInfo[0]].append([treeInfo[i], treeInfo[i+1]])

start = 1
visited = [False] * (V+1)
n1 = longest(start)

new_start = n1.index(max(n1[1:]))
visited = [False] * (V+1)
n2 = longest(new_start)

print(max(n2[1:]))