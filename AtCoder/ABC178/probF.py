import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

start = 0
ind = 0
NG = [0]*(2*N+1)

bdic = {}
for i, b in enumerate(B):
    if not b in bdic:
        bdic[b] = [i, i]
    else:
        bdic[b] = [min(bdic[b][0], i), max(bdic[b][1], i)]


for i, a in enumerate(A):
    if a in bdic:
        j1, j2 = bdic[a]
        if j1 >= i:
            NG[j1-i] += 1
            NG[j2-i+1] -= 1
        elif j2 < i:
            NG[j1-i+N] += 1
            NG[j2-i+1+N] -= 1
        else:
            NG[j1-i+N] += 1
            NG[0] += 1
            NG[j2-i+1] -= 1

start = -1
for i in range(N):
    if NG[i] == 0:
        start = i
        break
    NG[i+1] += NG[i]

if start == -1:
    print("No")
else:
    print("Yes")
    ans = []
    for i in range(N):
        ans.append(B[(i+start)%N])
    print(*ans)