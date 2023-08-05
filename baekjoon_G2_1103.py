'''
    제목 : 게임 (G2)
    문제 : 형택이는 1부터 9까지의 숫자와, 구멍이 있는 직사각형 보드에서 재밌는 게임을 한다.
            일단 보드의 가장 왼쪽 위에 동전을 하나 올려놓는다. 그다음에 다음과 같이 동전을 움직인다.
                1. 동전이 있는 곳에 쓰여 있는 숫자 X를 본다.
                2. 위, 아래, 왼쪽, 오른쪽 방향 중에 한가지를 고른다.
                3. 동전을 위에서 고른 방향으로 X만큼 움직인다. 이때, 중간에 있는 구멍은 무시한다.
            만약 동전이 구멍에 빠지거나, 보드의 바깥으로 나간다면 게임은 종료된다. 형택이는 이 재밌는 게임을 되도록이면 오래 하고 싶다.
            보드의 상태가 주어졌을 때, 형택이가 최대 몇 번 동전을 움직일 수 있는지 구하는 프로그램을 작성하시오.
    입력 :  줄에 보드의 세로 크기 N과 가로 크기 M이 주어진다. 이 값은 모두 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 보드의 상태가 주어진다. 쓰여 있는 숫자는 1부터 9까지의 자연수 또는 H이다. 가장 왼쪽 위칸은 H가 아니다. H는 구멍이다.
    출력 :  첫째 줄에 문제의 정답을 출력한다. 만약 형택이가 동전을 무한번 움직일 수 있다면 -1을 출력한다.
    
    풀이 :
        1. 형택이의 보드를 입력받는다
        2. 한 번 온 곳을 다시 왔을 경우 cycle이 생긴것. 방문한 위치에 대해 visited를 만들어 저장
        3. dp table을 만들어 각 위치까지 올 수 있는 횟수를 저장
        4. 스택에 경로를 저장하고 DFS 모든 경로를 돌고나서 종료
            스택 구조 : (row, column)
'''

from sys import stdin


def getBiggest(board):
    N, M = len(board), len(board[0])
    dp = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    stack = [(0, 0)]
    
    while stack:
        
        row, column = stack.pop()
        X = int(board[row][column])

        if visited[row][column]: return -1
        else : visited[row][column] = True
        
        if (column+X<M):
            if (board[row][column+X] != "H"):
                stack.append((row, column+X))
                dp[row][column+X] = max(dp[row][column+X] ,dp[row][column]+1)
        
            

        if (column-X>=0):
            if (board[row][column-X] != "H"):
                stack.append((row, column-X))
                dp[row][column-X] = max(dp[row][column-X] ,dp[row][column]+1)
        

        if (row+X<N):
            if (board[row+X][column] != "H"):
                stack.append((row+X, column))
                dp[row+X][column] = max(dp[row+X][column] ,dp[row][column]+1)
        

        if (row-X>=0): 
            if (board[row-X][column] != "H"):
                stack.append((row-X, column))
                dp[row-X][column] = max(dp[row-X][column] ,dp[row][column]+1)
        

        

    return max(map(max, dp)) +1



N, M = map(int, stdin.readline().split())

board = []
for _ in range(N):
    board.append(list(stdin.readline()[:-1]))

print(getBiggest(board))
