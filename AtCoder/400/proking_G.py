from collections import Counter

S = list(input())
A = Counter(S)

L = 0
c = 0
for v in A.values():
    L += v//2*2
    c += v%2
if c > 0:
    print((L+1)**2 + c-1)
else:
    print(L**2)