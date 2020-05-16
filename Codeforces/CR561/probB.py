K = int(input())

ok = False
for n in range(5, K):
    if K%n == 0 and K//n >= 5:
        ok = True
        m = K//n
        break

if not ok:
    print(-1)
else:
    alp = [
        'aiueo', 'oaiue', 'eoaiu', 'ueoai', 'iueoa'
    ]
    for i in range(5):
        alp[i] = alp[i]*(n//5) + alp[i][:n%5]
    ans = ''
    for j in range(m):
        ans += alp[j%5]
    print(ans)