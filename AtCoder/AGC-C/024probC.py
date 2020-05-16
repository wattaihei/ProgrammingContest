N = int(input())
A = [int(input()) for _ in range(N)]

ok = True
pre = -1
for i, a in enumerate(A):
    if a > pre + 1:
        ok = False
        break
    pre = a

if not ok:
    print(-1)
else:
    c = 0
    for i in range(N-1):
        if A[i+1] != A[i] + 1:
            c += A[i+1]
        else:
            c += 1
    print(c)