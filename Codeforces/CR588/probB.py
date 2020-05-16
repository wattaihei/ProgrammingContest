import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(input().rstrip())

ans = []
if N == 1:
    if K > 0:
        ans = ["0"]
    else:
        ans = S
else:
    if S[0] != "1":
        if K > 0:
            K -= 1
            ans.append("1")
        else:
            ans.append(S[0])
    else:
        ans.append("1")
    for i, s in enumerate(S):
        if i == 0: continue
        if S[i] != "0":
            if K > 0:
                ans.append("0")
                K -= 1
            else:
                ans.append(S[i])
        else:
            ans.append("0")

print("".join(ans))