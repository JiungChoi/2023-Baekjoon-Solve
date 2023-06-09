from sys import stdin
BAR_LENGTH = 64

X = int(stdin.readline())

now_bar = [BAR_LENGTH]
now_bar_size = sum(now_bar)
while(now_bar_size != X):
    a = now_bar.pop() / 2
    b = a
    now_bar_size = sum(now_bar)
    now_bar = now_bar + [a, b] if now_bar_size + a < X else now_bar + [a]
    now_bar_size = sum(now_bar)

print(len(now_bar))