'''
    제목 : 삼각형으로 자르기
    문제 : 볼록 다각형이 있고, 여기서 3개의 연속된 점을 선택해서 삼각형을 만든다. 그 다음, 만든 삼각형을 다각형에서 제외한다. 원래 다각형이 N개의 점이 있었다면, 이제 N-1개의 점으로 구성된 볼록 다각형이 된다. 위의 과정은 남은 다각형이 삼각형이 될 때까지 반복한다.
            볼록 다각형의 점이 시계 방향순으로 주어진다. 마지막에 남은 삼각형은 여러 가지가 있을 수 있다. 이때, 가능한 넓이의 최댓값을 구하는 프로그램을 작성하시오.
    입력 : 첫째 줄에 볼록 다각형 점의 수 N (3 ≤ N ≤ 35)이 주어진다. 둘째 줄부터 N개의 줄에는 볼록 다각형을 이루고 있는 점이 시계 방향 순서로 주어진다. 좌표는 10,000보다 작거나 같은 자연수이다.
    출력 : 첫째 줄에 문제의 정답을 출력한다. 절대/상대 오차는 10-9까지 허용한다.
    풀이 : 
        1. 삼각형 2차원 배열 형태로 받기
        2. 세 점이 주어졌을 때삼각형넓이 구하는 함수 : https://ladyang86.tistory.com/60
        3. 3차 반복문으로 중복 줄이고 (i: 1..N-2, j: i+1..N-1, k: j+1..N) 삼각형 최댓값 구하기
'''

from sys import stdin

def getArea(A, B, C):
    return 1/2*(abs((A[0]*B[1]+B[0]*C[1]+C[0]*A[1]) - (A[0]*C[1]+B[0]*A[1]+C[0]*B[1])))

def getWidest(polygon):
    area = 0
    length = len(polygon)
    for i in range(0, length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                area = max(area, getArea(polygon[i], polygon[j], polygon[k]))
    return area

N = int(stdin.readline())
polygon = []
for _ in range(N):
    polygon.append(list(map(int, stdin.readline().split())))

print(getWidest(polygon))
