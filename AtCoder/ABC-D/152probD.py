N = int(input())

st = [[0]*10 for _ in range(10)]
for n in range(1,N+1):
    if n%10==0:
        continue
    u = n%10
    d = int(str(n)[0])
    st[u][d] += 1

ans = 0
for n in range(1, N+1):
    if n%10==0:
        continue
    u = n%10
    d = int(str(n)[0])
    ans += st[d][u]

print(ans)