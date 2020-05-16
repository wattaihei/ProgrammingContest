import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
graph = [{} for _ in range(N)]
for _ in range(M):
    a, b, d = map(int, input().split())
    a -= 1; b -= 1
    if b in graph[a]:
        graph[a][b] += d
    else:
        graph[a][b] = d
    if a in graph[b]:
        graph[b][a] -= d
    else:
        graph[b][a] = -d

for n in range(N):
    Plus = []; Minus = []
    for m, d in graph[n].items():
        if d > 0:
            Plus.append((m, d))
        elif d < 0:
            Minus.append((m, -d))
    
    mi = 0
    for pm, pd in Plus:
        while pd > 0 and mi < len(Minus):
            mm, md = Minus[mi]
            if pd >= md:
                if mm in graph[pm]:
                    graph[pm][mm] -= md
                    graph[mm][pm] += md
                else:
                    graph[pm][mm] = -md
                    graph[mm][pm] = md
                del graph[n][mm]
                del graph[mm][n]
                pd -= md
                mi += 1
            else:
                if mm in graph[pm]:
                    graph[pm][mm] -= pd
                    graph[mm][pm] += pd
                else:
                    graph[pm][mm] = -pd
                    graph[mm][pm] = pd
                Minus[mi] = (mm, md-pd)
                pd = 0
        if pd == 0:
            del graph[n][pm]
            del graph[pm][n]
        else:
            graph[n][pm] = pd
            graph[pm][n] = -pd
    if mi < len(Minus):
        mm, md = Minus[mi]
        graph[n][mm] = -md
        graph[mm][n] = md

ans = []
for n in range(N):
    for m, d in graph[n].items():
        if d > 0:
            ans.append(str(n+1) + " " +  str(m+1) + " " + str(d))

print(len(ans))
print("\n".join(ans))