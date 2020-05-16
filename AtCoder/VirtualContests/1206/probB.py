A = int(input())
S = list(input())

ok = False
n = A
if n == 0: ok = True
for s in S:
    if s == '+':
        n += 1
    else:
        n -= 1
    if n == 0:
        ok = True
print("Yes" if ok else "No")