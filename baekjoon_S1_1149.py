# RGB 거리 (S1)

from sys import stdin

N = int(stdin.readline())

rgb_house = []
for _ in range(N):
    rgb_house.append(list(map(int, input().strip().split())))

for now in range(1, N):
    rgb_house[now][0] = min(rgb_house[now-1][1], rgb_house[now-1][2]) + rgb_house[now][0]
    rgb_house[now][1] = min(rgb_house[now-1][0], rgb_house[now-1][2]) + rgb_house[now][1]
    rgb_house[now][2] = min(rgb_house[now-1][0], rgb_house[now-1][1]) + rgb_house[now][2]

print(min(rgb_house[N-1]))


