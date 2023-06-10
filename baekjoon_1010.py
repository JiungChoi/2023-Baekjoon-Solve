from sys import stdin

def factorial(num):
    if num == 0 : return 1
    elif num==1 : return 1
    else: return num*factorial(num-1)
    

T = int(stdin.readline())

for _ in range(T):
    N, M = map(int, stdin.readline().split())
    print(int(factorial(M)/(factorial(M-N)*factorial(N))))
    