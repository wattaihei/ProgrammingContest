import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

if len(T) == 1 and T[0] in S:
    ans = -1
else:
    ans = 0
    wait = -1
    for i, s in enumerate(S):
        if i < wait: continue
        must = True
        for j, t in enumerate(T):
            if i+j == len(S) or t != S[i+j]:
                must = False
                break
        if must:
            ans += 1
            wait = i+len(T)-1
print(ans)