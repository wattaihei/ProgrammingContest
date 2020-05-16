N, K = map(int, input().split())

m = N // K

if K % 2 == 0:
    if 2*(N%K)>=K:
        ans = m**3 + (m+1)**3
    else:
        ans = 2 * m**3
else:
    ans = m**3

print(ans)