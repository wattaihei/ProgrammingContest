from collections import Counter

S = list(input())
N = len(S)
A = Counter(S)

odd = 0
for k in A.values():
    if k % 2 == 1:
        odd += 1

if odd == 0:
    print(N)
else:
    a = (N-odd)//2
    print(a//odd*2+1)