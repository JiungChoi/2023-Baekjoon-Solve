'''
제목 : 육각수 (G4)
    문제 : 육각수는 육각형을 이용해 정의할 수 있다. hn은 한 변에 점 1, 2, ..., n개가 있는 육각형을 점 하나만 겹치게 그렸을 때 존재하는 서로 다른 점의 개수이다. 첫 육각수 6개는 1, 6, 15, 28, 45, 66이다. 자연수 N이 주어졌을 때, 합이 N이 되는 육각수 개수의 최솟값을 구해보자. 1791보다 큰 정수는 항상 육각수 4개의 합으로 만들 수 있다. 또한, 수가 충분히 크다면 항상 육각수 3개의 합으로 만들 수 있다. 또, 최소 개수는 항상 6 이하이고, 이것이 최소인 N은 11과 26밖에 없다. 답이 6인 가장 큰 N은 26, 5인 가장 큰 N은 130, 4인 가장 큰 N은 146858이다.
    입력 : 첫째 줄에 N이 주어진다.
    출력 : 첫째 줄에 N을 만들기 위해 필요한 육각수 개수의 최솟값을 출력한다.
    제한 : 1 ≤ N ≤ 1,000,000

    풀이 : 
        1. N보다 작은 육각수의 리스트를 만듬
        2. 
        
'''
from sys import stdin

INF = 10 ** 6
dp = [0] + [INF] * 1000000

def get_hexes(N):
    x, now = 1, 0
    ans = []
    while now <= N:
        now = x * (2*x - 1)
        ans.append(now)
        x += 1
    return ans[:-1]

def how_many_hex(N):
    hexes = get_hexes(N)
    for i in range(1, N+1):
        min_val = INF
        for hex in hexes:
            if hex == i :
                min_val = 0
                break
            if hex > i: break
            min_val = min(min_val, dp[i-hex])
        dp[i] = min_val + 1
    print(dp[N])

N = int(stdin.readline())
how_many_hex(N)