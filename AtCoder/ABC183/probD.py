import sys
input = sys.stdin.buffer.readline

MAX = 3*10**5

N, W = map(int, input().rstrip().split())
STP = [list(map(int, input().rstrip().split())) for _ in range(N)]

A = [0]*MAX

for s, t, p in STP:
    A[s] += p
    A[t] -= p

now = 0
ok = True
for a in A:
    now += a
    if now > W:
        ok = False
        break

print("Yes" if ok else "No")