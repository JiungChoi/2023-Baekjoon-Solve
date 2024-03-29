'''
    제목 : 내멋대로 주사위 (G2)
    문제 : 
        진영이는 월드 카지노의 사장이다. 이번에 블랙잭의 신 최백준에게 거의 전 재산을 뺏기고 난 후에 어떻게 하면 다른 게임으로 돈을 되찾을까 고민하다가 새로운 주사위를 만들었다.
        진영이가 만든 이 주사위는 6면이고, 각 면에는 양의 정수가 쓰여져 있고, 모두 다른 숫자들이다. 그리고, 주사위에 쓰여 있는 숫자의 평균은 M을 넘을 수 없다.

        진영이가 원하는 주사위의 가능한 경우의 수를 구하는 프로그램을 작성하시오.
        주사위 A와 B가 있을 때, B를 회전시켜서 A를 얻을 수 있다면, A와 B는 같은 주사위라고 한다. 정답이 매우 커질 수 있으니 1,000,000,007로 나눈 나머지를 출력한다.
    입력 : 첫째 줄에 M이 주어진다. M은 1보다 크거나 같고, 1,000,000보다 작거나 같은 자연수이다.
    출력 : 문제의 정답을 1,000,000,007로 나눈 나머지를 출력한다.
    
    풀이 :
        1. 서로 다른 숫자 6개로 만들 수 있는 주사위 경우의 수 : 30개(6!/(6*4))
        2. 가능한 서로 다른 숫자 6개를 찾아 30을 곱함.
        3. 주어진 평균 M에 대해 크기가 M*6 +1 인 dp table을 만듬
        4. dp table의 각 인덱스는 평균이 아닌 합에대한 가능한 경우의 수가 채워짐
        5. 점화식 : 

'''

from sys import stdin

BUFFER = 1000000007

def getCnt(avr):
    return 1

def getPossibleCase(M):
    dp = [[] for _ in range(M*6 +1)]
    
    # 최소 주사위 눈이 1, 2, 3, 4, 5, 6 (합 21)는 되어야 경우의 수가 생김
    for i in range(0, 22):
        dp[i] = 0

    for i in range(6*M, 21, -1):
        dp[i] = 


    return dp[-1]

M = int(stdin.readline())
print(getPossibleCase(M))



