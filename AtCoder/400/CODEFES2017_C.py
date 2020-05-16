import sys
input = sys.stdin.readline

S = list(input().rstrip())
L = len(S)

T = []
Inds = [-1]
for i, s in enumerate(S):
    if s != "x":
        T.append(s)
        Inds.append(i)
Inds.append(L)

if T != T[::-1]:
    print(-1)
else:
    R = len(T)
    ans = 0
    for i in range((R+1)//2):
        l = Inds[i+1] - Inds[i]
        r = Inds[-i-1] - Inds[-i-2]
        ans += abs(r-l)
    print(ans)