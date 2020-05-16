N = int(input())
A = list(map(int, input().split())) # １行に別れてるとき

A1 = []
k = 0
for i in range(N):
    if i % 2 == 0:
        k += A[i]
    else:
        k -= A[i]
    A1.append(k)

ans = []
for i in range(N):
    if i == 0:
        ans.append(A1[-1])
        continue
    pre = A1[-1] - A1[i-1]
    fow = A1[i-1]
    if i % 2 == 0:
        ans.append(pre - fow)
    else:
        ans.append(fow - pre)

print(' '.join(map(str, ans)))