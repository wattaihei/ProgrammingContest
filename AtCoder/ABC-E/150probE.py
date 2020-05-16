import sys
input = sys.stdin.readline

mod = 10**9+7

N = int(input())
C = list(map(int, input().split()))

C.sort(reverse=True)

A = [1]
for _ in range(N):
    A.append(A[-1]*2%mod)

t = C[0]*A[N-1] % mod
for k in range(1, N):
    t = (t + C[k]*(A[N-1]+k*A[N-2])%mod) % mod
print(t*A[N]%mod)