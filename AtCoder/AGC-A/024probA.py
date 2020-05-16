import numpy as np

A ,B ,C, K = map(int, input().split())

q0 = np.matrix([A, B, C]).T
mat = np.matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]])

q1 = mat**K * q0
ans = q1[0, 0] - q1[1, 0]
if ans > 1E18:
    print('Unfair')
else:
    print(ans)