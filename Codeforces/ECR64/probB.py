from collections import Counter

Q = int(input())
Query = []
for _ in range(Q):
    S = list(input())
    Query.append(S)

alp = [chr(i) for i in range(97, 97+26)]

for S in Query:
    C = Counter(S)
    A = sorted(C.keys())
    B1 = []
    B2 = []
    for i, a in enumerate(A):
        if i % 2 == 0:
            B2.append(a)
        else:
            B1.append(a)
    if not B1:
        D = B2
    elif abs(alp.index(B1[-1])-alp.index(B2[0])) != 1:
        D = B1 + B2
    elif abs(alp.index(B1[0])-alp.index(B2[-1])) != 1:
        D = B2 + B1
    else:
        D = []
    if not D:
        print('No answer')
    else:
        ans = ''
        for d in D:
            ans += d*C[d]
        print(ans)