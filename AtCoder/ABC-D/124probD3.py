N, K = map(int, input().split())
S = list(input())

l = 0
r = 0
change = 0 if S[0] == '1' else 1
ans = 0
while l < N and r < N:
    #print(l, r, change)
    ans = max(ans, r-l+1)
    if r == N-1:
        break
    if S[r] == '0':
        r += 1
    else:
        if S[r+1] == '0':
            if change < K:
                change += 1
                r += 1
            else:
                if S[l] == '0' and S[l+1] == '1':
                    r += 1
                l += 1
        else:
            r += 1
print(ans)