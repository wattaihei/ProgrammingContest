import sys
input = sys.stdin.readline

N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
mod = 10**9+7

A = 0
for i in range(N-1):
    A += (X[i+1] - X[i])*((i+1)*(N-1-i)) % mod
    A %= mod

B = 0
for j in range(M-1):
    B += (Y[j+1]-Y[j])*((j+1)*(M-1-j)) % mod
    B %= mod

print(A*B%mod)