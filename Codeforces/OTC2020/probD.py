import sys
input = sys.stdin.readline
from copy import deepcopy

N = int(input())

def longest(s, graph, lo=False):
    D = [-1]*N
    D[s] = 0
    P = []
    for sp in graph[s]:
        D[sp] = 1
        q = [sp]
        last = sp
        while q:
            qq = []
            for p in q:
                for np in graph[p]:
                    if D[np] == -1:
                        last = np
                        D[np] = D[p] + 1
                        qq.append(np)
            q = qq
        P.append(last)
    if lo:
        d = -1
        p = -1
        for l in P:
            if D[l] > d:
                d = D[l]
                p = l
        return p
    if len(P) >= 2:
        return P[-2:]
    return P

def update(s1, s2, par, graph):
    D = [-1]*N
    D[par] = 0
    ngraph = deepcopy(graph)
    parP = []
    for sp in graph[par]:
        q = [sp]
        D[sp] = 1
        ok = (sp != s1 and sp != s2)
        while q:
            qq = []
            for p in q:
                for np in graph[p]:
                    if D[np] == -1:
                        if np == s1 or np == s2:
                            ok = False
                            break
                        D[np] = D[p] + 1
                        qq.append(np)
            q = qq
        if ok:
            parP.append(sp)
    ngraph[par] = parP
    return ngraph

def ask(u, v):
    print("?", u+1, v+1)
    sys.stdout.flush()
    n = int(input())
    return n-1

def main():

    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    s1 = longest(0, graph, lo=True)
    s2 = longest(s1, graph, lo=True)
    while s1 != -1:
        par = ask(s1, s2)
        graph = update(s1, s2, par, graph)
        P = longest(par, graph)
        if len(P) == 2:
            s1, s2 = P[0], P[1]
        elif len(P) == 1:
            s1, s2 = P[0], par
        else:
            s1, s2 = -1, par
    print("!", s2+1)

if __name__ == "__main__":
    main()