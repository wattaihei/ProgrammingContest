import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = input().rstrip()
AB = []
AA = []
BB = []
for _ in range(M):
    a, b = map(int, input().split())
    if S[a-1] == "A" and S[b-1] == "B":
        AB.append((a-1, b-1))
    elif S[a-1] == "B" and S[b-1] == "A":
        AB.append((b-1, a-1))
    elif S[a-1] == "A":
        AA.append((a-1, b-1))
    else:
        BB.append((a-1, b-1))

graph = [set() for _ in range(2*N)]
to_A = [False]*N
to_B = [False]*N

for a, b in AB:
    graph[a].add(b)
    graph[b+N].add(a+N)
    to_B[a] = True
    to_A[b] = True

for a, b in AA:
    if to_B[a] or to_B[b]:
        graph[b+N].add(a)
        graph[a+N].add(b)

for a, b in BB:
    if to_A[a] or to_A[b]:
        graph[a].add(b+N)
        graph[b].add(a+N)


Color = [-1]*(2*N)
loop = False

for n in range(2*N):
    if Color[n] != -1:
        continue
    stack = [n]
    Color[n] = n
    while stack:
        p = stack[-1]
        update = False
        for np in graph[p]:
            if Color[np] == -1:
                update = True
                Color[np] = n
                stack.append(np)
                break
            elif len(stack) > 1:
                if np != stack[-2] and Color[np] == n:
                    loop = True
                    break
        if not update:
            stack.pop()
            Color[p] = 10**14
        if loop:
            break
    if loop:
        break

print("Yes" if loop else "No")