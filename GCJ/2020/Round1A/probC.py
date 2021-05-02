import sys
input = sys.stdin.readline


def solve(R, C, state):
    N = R*C
    graph = [set() for _ in range(N)]

    S = 0
    for r in range(R):
        for c in range(C):
            S += state[r][c]
            n = r*C+c
            if r != 0:
                graph[n].add((r-1)*C+c)
            if r != R-1:
                graph[n].add((r+1)*C+c)
            if c != 0:
                graph[n].add(r*C+c-1)
            if c != C-1:
                graph[n].add(r*C+c+1)

    Vs = set([i for i in range(N)])
    score = 0
    while Vs:
        to_rem = set()
        for v in Vs:
            c = 0
            k = 0
            for n in graph[v]:
                c += 1
                k += state[n//C][n%C]
            if state[v//C][v%C]*c < k:
                to_rem.add(v)
        score += S
        Vs = set()
        for v in to_rem:
            vr, vc = v//C, v%C
            S -= state[vr][vc]
            sameR = []
            sameC = []
            for n in graph[v]:
                graph[n].remove(v)
                nr, nc = n//C, n%C
                if nr == vr:
                    sameR.append(nc)
                else:
                    sameC.append(nr)
                if not n in to_rem:
                    Vs.add(n)
            
            if len(sameR) == 2:
                c1, c2 = sameR
                n1, n2 = vr*C+c1, vr*C+c2
                graph[n1].add(n2)
                graph[n2].add(n1)
            if len(sameC) == 2:
                r1, r2 = sameC
                n1, n2 = r1*C+vc, r2*C+vc
                graph[n1].add(n2)
                graph[n2].add(n1)
    
    return score

def main():
    Q = int(input())
    Query = []
    for _ in range(Q):
        R, C = map(int, input().split())
        state = [list(map(int, input().split())) for _ in range(R)]
        Query.append((R, C, state))
    for qnum, (R, C, state) in enumerate(Query):
        ans = solve(R, C, state)
        print("Case #{0}: {1}".format(qnum+1, ans))


if __name__ == "__main__":
    main()