from math import sqrt

N = int(input())

s = 0
for n in range(1, int(sqrt(N))+2):
    if N%n == 0 and n <= N//n - 2:
        s += N//n-1
print(s)