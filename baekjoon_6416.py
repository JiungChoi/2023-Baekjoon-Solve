from sys import stdin

cns = True
while(cns != '-1 -1'):
    cns = stdin.readline().replace("\n", "  ").split("  ")
    print(f"n : {cns}")

data = [stdin.readline().strip() for i in range(n)]