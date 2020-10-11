import sys
input = sys.stdin.readline

MAX = 2001

N, P = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = []
for x in range(1, MAX+1):
    tmp = 1
    for i, a in enumerate(A):
        cantake = max(min(x+N-a, N)-i, 0)
        tmp = (tmp * cantake) % P
    if tmp != 0:
        ans.append(x)

print(len(ans))
print(*ans)