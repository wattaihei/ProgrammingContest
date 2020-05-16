import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

s = 0
pre = A[0]
S = []
for a in A:
    if a == pre:
        s += 1
    else:
        S.append(s)
        s = 1
    pre = a

if not S:
    print(-1)
else:
    if A[0] == A[-1]:
        S[0] += s
    else:
        S.append(s)
    
    ans = 1
    for s in S:
        ans = max(ans, (s+1)//2)
    print(ans)