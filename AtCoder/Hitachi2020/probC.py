import sys
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

Cl = [-1]*N
C = [[0], []]
q = [0]
c = 0
Cl[0] = 0
while q:
    qq = []
    c ^= 1
    for p in q:
        for np in graph[p]:
            if Cl[np]  == -1:
                Cl[np] = c
                C[c].append(np)
                qq.append(np)
    q = qq

if len(C[0]) > len(C[1]):
    C = [C[1], C[0]]

c0 = (N+2)//3
c1 = (N+1)//3
c2 = N//3
Co = [[], [], []]
if len(C[0]) < c1:
    R = set(C[0])
    for r in R:
        Co[2].append(r)
    for p in range(N):
        if p in R:
            continue
        elif len(Co[0]) < c0:
            Co[0].append(p)
        elif len(Co[1]) < c1:
            Co[1].append(p)
        else:
            Co[2].append(p)
# elif len(C[1]) < c1:
#     R = set(C[1])
#     for r in R:
#         Co[2].append(r)
#     for p in range(N):
#         if p in R:
#             continue
#         elif len(Co[0]) < c0:
#             Co[0].append(p)
#         elif len(Co[1]) < c1:
#             Co[1].append(p)
#         else:
#             Co[2].append(p)
else:
    R2 = set(C[1])
    for p in range(N):
        if p in R2: # larger
            if len(Co[0]) < c0:
                Co[0].append(p)
            else:
                Co[2].append(p)
        else: # smaller
            if len(Co[1]) < c1:
                Co[1].append(p)
            else:
                Co[2].append(p)

ans = [None]*N
for i, n in enumerate(Co[0]):
    ans[n] = 3*i+1
for i, n in enumerate(Co[1]):
    ans[n] = 3*i+2
for i, n in enumerate(Co[2]):
    ans[n] = 3*i+3


print(*ans)