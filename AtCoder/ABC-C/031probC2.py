N = int(input())
A = list(map(int, input().split()))

ans = -100000
for t in range(N):
    for a in range(N):
        St, Sa = 0, 0
        if a == t:
            continue
        if a > t:
            B = A[t:a+1]
        else:
            B = A[a:t+1]
        for ib, b in enumerate(B):
            if ib%2 == 0:
                St += b
            else:
                Sa += b
        if a == 0 or (t == 0 and a == 1):
            maxa = Sa
            maxt = St
            continue
        if Sa > maxa:
            maxa = Sa
            maxt = St
    ans = max(ans, maxt)
print(ans)