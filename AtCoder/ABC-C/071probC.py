import collections

N = int(input())
A = list(map(int, input().split()))

B = collections.Counter(A)

p = []
for k, v in B.items():
    if v >= 2:
        p.append(k)
    if v >= 4:
        p.append(k)

if len(p) < 2:
    print(0)
else:
    p.sort()
    print(p[-1]*p[-2])