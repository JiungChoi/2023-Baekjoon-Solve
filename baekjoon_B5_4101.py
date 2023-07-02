# 크냐? (B5)

from sys import stdin


while True:
    num1, num2 = map(int, stdin.readline().split())
    if num1 == 0 and num2 == 0: break
    
    print("Yes") if num1>num2 else print("No")