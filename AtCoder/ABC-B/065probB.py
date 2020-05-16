N = int(input())
A = [int(input()) for _ in range(N)]

c = 0
n = 1
checked = [False for _ in range(N)]
checked[0] = True
for _ in range(N+1):
    n = A[n-1]
    c += 1
    if n == 2:
        ok = True
        break
    if checked[n-1]:
        ok = False
        break
    checked[n-1] = True
if ok:
    print(c)
else:
    print(-1)