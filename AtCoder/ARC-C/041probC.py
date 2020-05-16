import sys
input = sys.stdin.readline

N, Le = map(int, input().split())
Pairs = []
LR = []
L = []
R = [0]
dir = "R"
for i in range(N):
    strX, d = input().rstrip().split()
    X = int(strX)
    if d == "R":
        if dir == "L":
            LR.append(L)
            Pairs.append(LR)
            LR = []
            R = [X]
            dir = "R"
        elif i == 0:
            R = [X]
        else:
            R.append(X)
    else:
        if dir == "R":
            LR.append(R)
            L = [X]
            dir = "L"
        else:
            L.append(X)
if dir == "L":
    LR.append(L)
    Pairs.append(LR)
else:
    LR.append(R)
    LR.append([Le+1])
    Pairs.append(LR)

ans = 0
for R, L in Pairs:
    min_L = L[0]
    for i, l in enumerate(L):
        ans += l-min_L-i
    max_R = R[-1]
    for i, r in enumerate(R):
        ans += max_R-r-(len(R)-i-1)
    ans += (min_L-max_R-1)*max(len(R), len(L))

print(ans)