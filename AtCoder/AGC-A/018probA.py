N, K = map(int, input().split()) # 横に2個
A = list(map(int, input().split()))

A.sort(reverse=True)

dif = []
for i in range(N-1):
    d = A[i] - A[i+1]
    if d != 0:
        dif.append(d)
if dif:
    mind = min(dif)
else:
    mind = A[0]

ans = 'IMPOSSIBLE'
for a in A:
    if a < K:
        break
    if a == K:
        ans = 'POSSIBLE'
        break
    if (a-K) % mind == 0:
        ans = 'POSSIBLE'
        break

print(ans)