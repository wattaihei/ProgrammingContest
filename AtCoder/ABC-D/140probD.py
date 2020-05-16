N, K = map(int, input().split())
S = list(input())

sl = 0
for i in range(N-1, -1, -1):
    if S[i] == S[0]:
        sr = i
        break
    else:
        sl += 1
if sl == 0:
    sl = 1

only = True
for s in S:
    if s != S[0]:
        only = False
        break

if only:
    ans = N-1
else:
    r = sr
    l = 0
    change = 0
    while l<=r and change <= K:
        if S[l] != S[l+1]:
            if S[r] != S[r-1]:
                change += 1
                l += 1
                r -= 1
            else:
                r -= 1
        else:
            l += 1
    if change < K:
        ans = N-1
    elif change == K:
        ans = sr + sl-1
    else:
        ans = l-1 + (sr-r-1) + sl-1
        for i in range(l, r):
            if S[i] == S[i+1]:
                ans += 1
print(ans)