import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(K):
    Imos = [0]*(N+1)
    for i, a in enumerate(A):
        Imos[max(0, i-a)] += 1
        Imos[min(N, i+a+1)] -= 1
    B = [0]*(N)
    b = 0
    for i in range(N):
        b += Imos[i]
        B[i] = b
    if A == B:
        break
    A = B

print(*A)