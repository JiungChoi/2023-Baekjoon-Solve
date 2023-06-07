from sys import stdin
import math
A, B, V = map(int, stdin.readline().split())
print( 1 if A >= V else ( int(math.ceil((V-A) / (A-B))) + 1 if V > (2*A-B) else int(math.floor((V-A) / (A-B))) + 2 ))