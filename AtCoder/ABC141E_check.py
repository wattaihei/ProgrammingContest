# 文字列in文字列の計算量検証

import matplotlib.pyplot as plt
import random
import time

alpha = [chr(ord('a')+ i) for i in range(26)]

T = []
L1 = []
L2 = []
L = []
M = []


for i in range(22):
    for j in range(i, 22):
        l1 = 2**i
        l2 = 2**j + 1
        S1 = ''.join(random.choices(alpha, k=l1))
        S2 = ''.join(random.choices(alpha, k=l2))
        t0 = time.time()
        ok = False
        if S1 in S2:
            ok = True
        deltat = time.time() - t0
        print(l1, l2, deltat)
        T.append(deltat)
        L1.append(l1)
        L2.append(l2)
        L.append(l1+l2)
        M.append(l1*l2)

plt.title('time to do \'S1 in S2\'')

#plt.subplot(221)
plt.scatter(L, T, color='blue', label='len(S2)+len(S1)')
plt.xscale('log')
plt.yscale('log')
plt.ylim([1E-7, 1E-1])

plt.ylabel('time [s]')
plt.xlabel('len(S2)+len(S1)')
plt.grid()

"""
plt.subplot(222)
plt.scatter(M, T, color='green', label='len(S2)*len(S1)')
plt.xscale('log')
plt.yscale('log')
plt.ylim([1E-7, 1E-1])
#plt.title('time to do S1 in S2')
plt.ylabel('time [s]')
plt.xlabel('len(S2)*len(S1)')
plt.grid()

plt.subplot(223)
plt.scatter(L2, T, color='yellow', label='len(S2)')
plt.xscale('log')
plt.yscale('log')
plt.ylim([1E-7, 1E-1])
#plt.title('time to do S1 in S2')
plt.ylabel('time [s]')
plt.xlabel('len(S2)')
plt.grid()

plt.subplot(224)
plt.scatter(L1, T, color='brown', label='len(S1)')
plt.xscale('log')
plt.yscale('log')
plt.ylim([1E-7, 1E-1])
#plt.title('time to do S1 in S2')
plt.ylabel('time [s]')
plt.xlabel('len(S1)')
plt.grid()
"""

#plt.tight_layout()
plt.show()
        