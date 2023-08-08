'''
제목 : 친구 (S2)
    문제 : 지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다. 어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다. 여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.
            A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.
    입력 : 첫째 줄에 사람의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다.
    출력 : 첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력한다.

    풀이 : 
        1. 
        2. 
        
'''

from sys import stdin

def GetMostNumberOfFriend(grp):
    print(grp)
    return 1



N = int(stdin.readline())
graph = [[] for _ in range(N+1)]

for personA in range(1, N+1):
    friendAry = stdin.readline()
    for personB, isFriend in enumerate(friendAry):
        if isFriend == 'Y':
            if "Y" in graph[personA]: continue
            graph[personA].append(personB+1)
            graph[personB+1].append(personA)


print(GetMostNumberOfFriend(grp=graph))


import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
# 2-친구 사이일 때 1, 아니면 0
f = [[0] * n for _ in range(n)]

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      # 2-친구인 경우
      if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] =='Y'):
        f[i][j] = 1

res = 0

for row in f:
  res = max(res,sum(row))
print(res)
