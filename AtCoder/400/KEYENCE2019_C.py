N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0
O = []
c = 0
for i in range(N):
    if A[i] < B[i]:
        S += B[i] - A[i]
        c += 1
    else:
        O.append(A[i]-B[i])
if c == 0:
    ok = True
if c != 0:
    O.sort(reverse=True)
    a = 0
    ok = False
    for o in O:
        a += o
        c += 1
        if a >= S:
            ok = True
            break

if ok:
    print(c)
else:
    print(-1)