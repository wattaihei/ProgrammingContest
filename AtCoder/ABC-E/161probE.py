import sys
input = sys.stdin.readline

N, K, C = map(int, input().split())
S = list(input().rstrip())

A = [0]
go = C
for s in S:
    if go >= C:
        if s == "o":
            A.append(A[-1]+1)
            go = 0
        else:
            A.append(A[-1])
    else:
        go += 1
        A.append(A[-1])

B = [0]*(N+1)
go = C
for i in reversed(range(N)):
    s = S[i]
    if go >= C:
        if s == "o":
            B[i] = B[i+1]+1
            go = 0
        else:
            B[i] = B[i+1]
    else:
        go += 1
        B[i] = B[i+1]

ans = []
for n in range(N):
    if S[n] == "o" and A[n] + B[n+1] < K:
        ans.append(str(n+1))

print("\n".join(ans))