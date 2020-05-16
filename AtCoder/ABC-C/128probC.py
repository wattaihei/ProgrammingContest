import numpy as np


N, M = map(int, input().split())
s_mat = np.zeros((M, N), dtype=int)
si_list = []
for i in range(M):
    si = list(map(int, input().split()))[1:]
    for s in si:
        s_mat[i, s-1] = 1
p_list = np.array(list(map(int, input().split())))


prob = 0
for i in range(2**N):
    i_list = []
    for k in range(N-1, -1, -1):
        if i >= 2**k:
            amari = 1
            i -= 2**k
        else:
            amari = 0
        i_list.append(amari)
        
    i_array = s_mat.dot(np.array(i_list)) % 2
    if np.all(i_array == p_list):
        prob += 1

print(prob)
