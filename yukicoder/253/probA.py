import sys
input = sys.stdin.readline

mod = 10**9+7

N = int(input())
A = list(map(int, input().split()))

while len(A) > 1:
    B = []
    for i in range(len(A)-1):
        B.append((A[i]+A[i+1])%mod)
    A = B

print(A[0])