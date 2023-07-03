# 새 (B2)

from sys import stdin

N = int(stdin.readline())

cnt, ans = 0, 0
while N>0:
    cnt += 1
    ans +=1 
    if N < cnt: cnt = 1
    N -= cnt

print(ans)