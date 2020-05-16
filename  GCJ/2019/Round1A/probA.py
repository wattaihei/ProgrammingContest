import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]


for qnum, (R, C) in enumerate(Query):
    graph = [[] for _ in range(R*C)]
    for nr in range(R):
        for nc in range(C):
            n = C*nr + nc
            for mr in range(R):
                for mc in range(C):
                    m = C*mr + mc
                    if nr != mr and nc != mc and (nr+nc) != (mr+mc) and (nr-nc) != (mr-mc):
                        graph[n].append(m)
    
    for s in range(R*C):
        
