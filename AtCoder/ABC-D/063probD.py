N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]

H.sort(reverse=True)

L = B*(N-1) + A
c = H[-1] - H[-1]%L
ans = (H[-1]//L)*N

for i in range(N):
    H[i] -= (H[-1]//L)*L
print(H)
init = H[0]-A
d = B
for i, h in enumerate(H):
    if i == 0:
        ans += 1
        continue
    if max(init, h-d) <= 0:
        break
    init -= B
    d += B
    ans += 1

print(ans)