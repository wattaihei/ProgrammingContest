N = int(input())
LMN = [list(map(int, input().split())) for _ in range(N)]

A = [0, 0, 0]
for L in LMN:
    L.sort()
    for i in range(3):
        A[i] = max(A[i], L[i])

print(A[0]*A[1]*A[2])