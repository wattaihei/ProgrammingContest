import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = [0]*(N+1)
Q = [0]*(N+1)

for _ in range(M):
    f, b = map(str, input().rstrip().split())
    a = int(f)
    if b == "WA":
        if not Q[a]:
            P[a] += 1
    else:
        Q[a] = 1

p = 0
for i in range(N+1):
    if Q[i]:
        p += P[i]
print(sum(Q), p)