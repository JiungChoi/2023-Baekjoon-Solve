from sys import stdin

N, B = stdin.readline().split()

alpha_dict = {chr(asci):asci-55 for asci in range(65, 91)}
for i in range(10):
    alpha_dict[f"{i}"] = i

lenth, sum = len(N), 0
B = int(B)
for pos in range(lenth):
    sum += alpha_dict[f"{N[pos]}"] * B ** (lenth-pos-1)

print(sum)