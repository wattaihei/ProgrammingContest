from collections import Counter

S = list(input())

dic = Counter(S)
ok = True
A = list(dic.values())
a = A[0]
for c in A:
    if c != a:
        ok = False
print("Yes" if ok else "No")