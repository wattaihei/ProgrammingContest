import sys
input = sys.stdin.buffer.readline


N, D = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

B = [0]*(N-1)
for i in range(N-1):
    B[i] = A[i] - A[i+1] + D

C = [0]*(N-1)
for i in range(N-1):
    C[i] = A[i+1] - A[i] + D

dp1 = [0]*N
for i in range(N-1):
    dp1[i+1] = min(dp1[i] + B[i], 0)

dp2 = [0]*N
for i in reversed(range(N-1)):
    dp2[i] = min(dp2[i+1]+C[i], 0)

ans = 2*sum(A) - A[0] - A[-1] + D*(N-1)
for i in range(1, N-1):
    ans += min(dp1[i], dp2[i])

print(ans)