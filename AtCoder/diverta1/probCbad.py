import numpy as np

N = int(input())
s = [input() for _ in range(N)]


ABarray = np.zeros((N, 2), dtype=int)
count = 0
for i, alp in enumerate(s):
    ABarray[i, 0] = 1 if (alp[-1] == 'A') else 0
    ABarray[i, 1] = 1 if (alp[0] == 'B') else 0
    count += alp.count('AB')

both = np.count_nonzero(np.all(ABarray == 1, axis=1))
ABsum = np.sum(ABarray, axis=0)
Aonly = ABsum[0] - both
Bonly = ABsum[1] - both

if Aonly == 0 and Bonly == 0 and both >= 1:
    count += both - 1
else:
    count += min(Aonly, Bonly) + both
print(count)
