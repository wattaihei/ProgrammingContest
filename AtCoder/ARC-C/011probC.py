import sys
input = sys.stdin.readline

s, g = map(str, input().split())
N = int(input())
S = [input().rstrip() for _ in range(N)]
L = len(S[0])

graph = [[] for _ in range(N+2)]
for i in range(N-1):
    for j in range(i, N):
        s1, s2 = S[i], S[j]
        c = 0
        for l in range(L):
            if s1[l] != s2[l]:
                c += 1
        if c <= 1:
            graph[i].append(j)
            graph[j].append(i)

for i in range(N):
    s0 = S[i]
    C = [0, 0]
    for l in range(L):
        if s[l] != s0[l]:
            C[0] += 1
        if g[l] != s0[l]:
            C[1] += 1
    if C[0] <= 1:
        graph[N].append(i)
    if C[1] <= 1:
        graph[i].append(N+1)

c = 0
for l in range(L):
    if s[l] != g[l]:
        c += 1
if c <= 1:
    graph[N].append(N+1)

q = [N]
checked = [False]*(N+2)
before = [None]*(N+2)
checked[N] = True
while q:
    qq = []
    for p in q:
        for np in graph[p]:
            if not checked[np]:
                checked[np] = True
                before[np] = p
                qq.append(np)
    if checked[N+1]:
        break
    q = qq

if not checked[N+1]:
    print(-1)
else:
    ans = [g]
    p = N+1
    while True:
        p = before[p]
        if p == N:
            ans.append(s)
            break
        ans.append(S[p])
    ans = ans[::-1]
    print(len(ans)-2)
    for a in ans:
        print(a)