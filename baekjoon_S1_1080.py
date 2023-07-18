'''
    제목 : 행렬 (S1, greedy)
    문제 : 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.
            행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)
    입력 :  첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.
    출력 :  첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.
    
    풀이 :
            1. 3x3 window를 행과 열에 대해 각각 0에서 N-3, 0에서 M-3 까지 2D 슬라이딩
            2. 행렬 A와 B에 대하여 현재 window의 (0,0) 위치에 해당하는 값을 비교
            3. 만약 두 값이 다르다면 현재 window 영역에 대한 A행렬 값을 반전 (1-now)
            4. 반전시킨 후 cnt+=1, 윈도우가 슬라이딩을 마칠 때 cnt 값이 A행렬을 B행렬로 만들기 위한 연산의 최솟값
        
'''

from sys import stdin

def reverse(i, j):
    for y in range(i, i+3):
        for x in range(j, j+3):
            A[y][x] = 1 - A[y][x]

N, M = map(int, stdin.readline().split())

matrix = []
for _ in range(2*N):
    matrix.append(list(map(int, stdin.readline()[:-1])))


A = matrix[:N]
B = matrix[N:]

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            reverse(i, j)
            cnt += 1

print(cnt if A==B else "-1")



