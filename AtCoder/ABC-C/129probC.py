import numpy as np

N, M = map(int, input().split())
a = np.array([int(input()) for _ in range(M)])

A = np.array([[0, 1], [1, 1]])
B = np.array([[0, 1], [0, 0]])

ans = np.array([1, 0 if (1 in a) else 1])

for j in range(2, N+1):
    ans = B.dot(ans) if j in a else A.dot(ans)

print(ans[-1] % 1000000007)