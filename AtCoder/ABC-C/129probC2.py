import numpy as np

N, M = map(int, input().split())
A = [1]*(N+1)
for _ in range(M):
    A[int(input())] = 0

step0 = 1
step1 = A[1]

ans = [step0, step1]
for i in range(2, N+1):
    now = (ans[-1] + ans[-2]) * A[i]
    ans.append(now)
print(ans[-1] % 1000000007)
