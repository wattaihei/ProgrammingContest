import numpy as np

S = np.array([int(i) for i in list(input())])
N = len(S)

def zebra(A):
    for _ in range(N-1):
        if A[-1] == 0:
            A.append(1)
        elif A[-1] == 1:
            A.append(0)
    return A

A0 = np.array(zebra([0]))
A1 = np.array(zebra([1]))

dis0 = np.count_nonzero(S - A0)
dis1 = np.count_nonzero(S - A1)

print(min(dis0, dis1))