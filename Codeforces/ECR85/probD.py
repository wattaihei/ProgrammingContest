import sys
input = sys.stdin.buffer.readline
from bisect import bisect_left

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]


B = [0]
for i in range(1, 2*10**5):
    B.append(i*(i+1)//2)

def solve(n, N):
    M = N*(N-1)
    n %= M
    if n%2 == 0:
        rem = (M - n)//2
        ind = bisect_left(B, rem)
        return N-ind
    else:
        rem = (M - (n-1))//2
        ind = bisect_left(B, rem)
        seq = rem - ind*(ind-1)//2
        return N - seq + 1


for N, L, R in Query:
    ans = []
    for n in range(L-1, R):
        ans.append(str(solve(n, N)))
    print(" ".join(ans))    