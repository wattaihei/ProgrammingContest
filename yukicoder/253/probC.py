import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))


A.sort(reverse=True)
ans = 0
for bit in range(1<<N):
    p = K
    for i in range(N):
        if bit&(1<<i):
            p %= A[i]
    p %= A[-1]
    ans = max(ans, p)

print(ans)