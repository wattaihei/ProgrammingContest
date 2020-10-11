import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())

A1 = [0]*(N+1)
A2 = [0]*(N+1)

t = 0
for i, s in enumerate(S):
    if s == "W":
        t += 1
    A1[i+1] = t

t = 0
for i in reversed(range(N)):
    if S[i] == "R":
        t += 1
    A2[i] = t

ans = 10**18
for a1, a2 in zip(A1, A2):
    score = abs(a1-a2) + min(a1, a2)
    ans = min(ans, score)

print(ans)