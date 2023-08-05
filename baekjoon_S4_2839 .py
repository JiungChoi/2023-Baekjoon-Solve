from sys import stdin


def HowManyPlasticBag(N):
    dp = [50000 for _ in range(N+1)]

    if N<3 : return -1
    elif N==3 : return 1
    elif N==4 : return -1

    dp[3] = 1
    dp[5] = 1

    for i in range(5, N+1):
        if i%3 == 0:
            dp[i] = min(dp[i], i//3)    
        if i%5 == 0:
            dp[i] = min(dp[i], i//5) 

        dp[i] = min(dp[i], dp[i-5]+1)
        dp[i] = min(dp[i], dp[i-3]+1)        
        
    return -1 if dp[-1] > 5000 else dp[-1] 

N = int(stdin.readline())

print(HowManyPlasticBag(N))