import sys
input = sys.stdin.readline

K, N = map(int, input().split())
A = list(map(int, input().split()))

m = 0
for i in range(N):
    m = max(m, (A[i]-A[i-1])%K)
print(K-m)