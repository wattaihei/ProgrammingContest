import math
N = int(input())

ans = N+1
for n in range(1, int(math.sqrt(N))+2):
    if N % n == 0:
        ans = min(ans, N//n+n-2)
print(ans)