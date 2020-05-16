import sys
input = sys.stdin.readline
import math

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    ans = set()
    T = int(math.sqrt(N))+2
    for n in range(T):
        if n**2 <= N:
            ans.add(n)
    for n in range(1,T):
        ans.add(N//n)
    A = sorted(list(ans))
    print(len(A))
    print(*A)