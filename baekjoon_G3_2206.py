import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def go():
    ## 현재 좌표 0 0 0 설정
    q.append([0, 0, 0])
    c[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        ## x >> 1 , -1 | y>> 1, -1 | 4가지 케이스 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if place[nx][ny] == 0 and c[nx][ny][z] == -1:
                    c[nx][ny][z] = c[x][y][z] + 1
                    q.append([nx, ny, z])
                elif z == 0 and place[nx][ny] == 1 and c[nx][ny][z+1] == -1:
                    c[nx][ny][z+1] = c[x][y][z] + 1
                    q.append([nx, ny, z+1])


N, M = map(int, sys.stdin.readline().split())
## 지도생성
place = [list(map(int,input())) for _ in range(N)]
## 비교 테이블 생성 _ [][]좌표 + [거리1,거리2] >> 거리2에 할당 시 벽을 깼다는 것
c = [[[-1]*2 for _ in range(M)] for _ in range(N)]
## 현재 좌표
q = deque()

go()
ans1, ans2 = c[N-1][M-1][0], c[N-1][M-1][1]
if ans1 == -1 and ans2 != -1:
    print(ans2)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))