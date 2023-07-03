# 방번호 (G3)

from sys import stdin

INF = 5001

N = int(stdin.readline())
ary = list(map(int, stdin.readline().split()))
M = int(stdin.readline())

dp = [-INF for _ in range(M+1)]

for i in range(N-1, -1, -1):
    x = ary[i]
    for j in range(x, M+1):
        dp[j] = max(dp[j], dp[j-x]*10+i, i)

print(dp[M])