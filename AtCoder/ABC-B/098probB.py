from collections import Counter

N = int(input())
S = list(input())
ans = 0
for i in range(N):
    L = list(Counter(S[:i]).keys())
    R = list(Counter(S[i:]).keys())
    c = 0
    for l in L:
        if l in R:
            c += 1
    ans = max(ans, c)
print(ans)