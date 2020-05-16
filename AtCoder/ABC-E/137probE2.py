import sys
input = sys.stdin.readline

def main():
    N, M, P = map(int, input().split())
    Edges = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**18

    graph1 = [[] for _ in range(N+1)]
    graph2 = [[] for _ in range(N+1)]
    for a, b, c in Edges:
        graph1[a].append(b)
        graph2[b].append(a)

    checked1 = [False]*(N+1)
    checked1[1] = True
    q = [1]
    while q:
        qq = []
        for p in q:
            for np in graph1[p]:
                if not checked1[np]:
                    checked1[np] = True
                    qq.append(np)
        q = qq
    
    checked2 = [False]*(N+1)
    checked2[N] = True
    q = [N]
    while q:
        qq = []
        for p in q:
            for np in graph2[p]:
                if not checked2[np]:
                    checked2[np] = True
                    qq.append(np)
        q = qq
    
    Canuse = [False]*(N+1)
    for i in range(1, N+1):
        if checked1[i] and checked2[i]:
            Canuse[i] = True



    D = [INF for _ in range(N+1)]
    D[1] = 0
    for i in range(2*N+100):
        update = False
        for a, b, c in Edges:
            if not Canuse[a] or not Canuse[b]: continue
            if D[b] > D[a] + P - c:
                D[b] = D[a] + P - c
                update = True


    if update:
        print(-1)
    else:
        print(max(-D[N], 0))

if __name__ == "__main__":
    main()