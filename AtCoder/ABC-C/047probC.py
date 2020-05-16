S = input()

ans = 0
pre = S[0]
for s in S:
    if pre != s:
        ans += 1
    pre = s
print(ans)