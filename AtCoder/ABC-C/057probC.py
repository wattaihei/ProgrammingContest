import math

N = int(input())

tmp = int(math.sqrt(N)) + 1

for n in range(1, tmp+1):
    if N % n == 0:
        a = N//n
print(len(str(a)))