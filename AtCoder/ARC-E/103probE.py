S = [int(a) for a in list(input())]
L = len(S)

ok = True
if S[L-1] == 1 or S[0] == 0 or S[L-2] == 0:
    ok = False
for i in range(L-1):
    if S[i] != S[L-2-i]:
        ok = False

if not ok:
    print(-1)
else:
    graph = []
    p = 1
    go = True
    for i in range(1, L):
        if i <= L//2:
            graph.append((p, i+1))
            if go:
                p = i+1
            if S[i] == 1:            
                go = True
            else:
                go = False
        else:
            graph.append((p, i+1))
    
    for a, b in graph:
        print(a, b)
        
