import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())
Ls = [list(map(int, input().split())) for _ in range(N)]

MA = 250
D = []
for s, (a, b) in zip(S, Ls):
    t = int(s)
    A = [t]*b
    t ^= 1
    tmp = 0
    for _ in range(MA-b):
        A.append(t)
        tmp += 1
        if tmp == a:
            tmp = 0
            t ^= 1
    D.append(A)

ans = 0
for i in range(MA):
    c = 0
    for n in range(N):
        c += D[n][i]
    ans = max(c, ans)
print(ans)