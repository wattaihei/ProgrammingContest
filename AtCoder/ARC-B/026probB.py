import math
N = int(input())
S = 1
for n in range(2, int(math.sqrt(N))+2):
    if N%n == 0:
        if N//n == n:
            S += n
        elif N//n > n:
            S += N//n + n
if N == 1:
    print('Deficient')
elif S == N:
    print('Perfect')
elif S < N:
    print('Deficient')
else:
    print('Abundant')