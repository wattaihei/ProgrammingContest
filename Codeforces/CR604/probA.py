import sys
input = sys.stdin.readline

Q = int(input())
Query = [input().rstrip() for _ in range(Q)]

for S in Query:
    L = len(S)
    ans = []
    ok = True
    pre = "?"
    for i in range(L-1):
        if S[i] == "?":
            for t in "abc":
                if t != pre and t != S[i+1]:
                    ans.append(t)
                    pre = t
                    break
        elif S[i] == S[i+1]:
            ok = False
            break
        else:
            pre = S[i]
            ans.append(S[i])
    if S[-1] == "?":
        for t in "abc":
            if t != pre:
                ans.append(t)
                break
    else:
        ans.append(S[-1])
    if ok:
        print("".join(ans))
    else:
        print(-1)