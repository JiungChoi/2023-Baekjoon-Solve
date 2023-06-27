# 트리의 지름 : 너비기반 탐색 (BFS)
from sys import stdin
INF = -1

def longest(start):
    distance = [INF]*(n+1)
    queue = []
    
    queue.append([start, 0])
    distance[start] = 0

    while queue:
        node, cost = queue[0]
        queue = queue[1:] if queue else []

        for next_node, next_cost in tree[node]:
            if distance[next_node] == -1:
                next_cost += cost
                distance[next_node] = next_cost
                queue.append([next_node, next_cost])

    return distance

n = int(stdin.readline())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, cost = map(int, stdin.readline().split())
    tree[parent].append([child, cost])
    tree[child].append([parent, cost])



start = 1
n1 = longest(start)

new_start = n1.index(max(n1[1:]))
n2 = longest(new_start)

print(max(n2[1:]))
