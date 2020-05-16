N, M = map(int, input().split())
L = []
R = []
for _ in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

answer = max([min(R) - max(L) + 1, 0])
print(answer)