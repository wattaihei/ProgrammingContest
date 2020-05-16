import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))

graph = [[] for _ in range(N)]
q1 = []
q2 = []
for i, a in enumerate(A):
    if i-a >= 0:
        graph[i-a].append(i)
    if i+a <= N-1:
        graph[i+a].append(i)
    if a%2 == 1:
        q1.append(i)
    else:
        q2.append(i)


D = [-1]*N
d = 0
while q1:
    qq = []
    d += 1
    for p in q1:
        for np in graph[p]:
            if D[np] == -1 and A[np]%2 == 0:
                D[np] = d
                qq.append(np)
    q1 = qq

d = 0
while q2:
    qq = []
    d += 1
    for p in q2:
        for np in graph[p]:
            if D[np] == -1 and A[np]%2 == 1:
                D[np] = d
                qq.append(np)
    q2 = qq

print(*D)