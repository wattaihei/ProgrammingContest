import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

S = 0
for i in range(K):
    S += (A[i]+1)/2
ans = S
for i in range(N-K):
    S += (A[i+K]+1)/2 - (A[i]+1)/2
    ans = max(ans, S)
print(ans)