from collections import Counter
from operator import itemgetter

Q = int(input())
data = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    data.append([N, A])

for N, A in data:
    A.sort()
    B = list(Counter(A).items())
    B.sort(key=itemgetter(0))
    ok = False
    a = 0
    for k, n in B:
        if k == 2048:
            ok = True
        if k < 2048:
            a += k*n
    if a >= 2048 or ok:
        print('YES')
    else:
        print('NO')