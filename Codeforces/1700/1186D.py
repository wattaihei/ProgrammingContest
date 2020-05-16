N = int(input())
A = [float(input()) for _ in range(N)]

ans = [None]*N
can = []
for i, a in enumerate(A):
    if a >= 0 or float(int(a)) == a:
        ans[i] = int(a)
    else:
        ans[i] = int(a) - 1
    if float(int(a)) != a:
        can.append(i)

delta = -sum(ans)
for j in range(delta):
    ans[can[j]] += 1

for a in ans:
    print(a)