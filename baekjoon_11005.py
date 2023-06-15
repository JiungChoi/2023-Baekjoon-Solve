# 진법변환 : 10진법(N) -> B진법
from sys import stdin

N, B = map(int, stdin.readline().split())

alpha_dict = {asci-55:chr(asci) for asci in range(65, 91)}
for i in range(10):
    alpha_dict[i] = f"{i}"

mok, namerge = N, 1
result = ''
while(mok):
    mok, namerge = mok//B , mok%B
    result += alpha_dict[namerge]

print(result[::-1])