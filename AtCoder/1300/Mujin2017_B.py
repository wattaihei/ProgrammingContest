import sys
input = sys.stdin.readline

N = int(input())
state = [list(input().rstrip()) for _ in range(N)]

ColState = [0]*N
fullcols = 0
for w in range(N):
    isfull = True
    isempty = True
    for h in range(N):
        if state[h][w] == "#":
            isempty = False
        else:
            isfull = False
    if isfull:
        fullcols += 1
    if isempty:
        ColState[w] = -1

ans = 10**14
for h in range(N):
    emp = 0
    for w in range(N):
        if state[h][w] == ".":
            emp += 1
    if ColState[h] == -1:
        emp += 1
    ans = min(ans, emp+(N-fullcols))

if ans == 2*N+1:
    print(-1)
else:
    print(ans)