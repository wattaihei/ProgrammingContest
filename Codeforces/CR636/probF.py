import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    state = [list(map(int, input().split())) for _ in range(N-1)]
    Query.append((N, state))

for N, state in Query:
    S = [[] for _ in range(N+1)]
    for i, A in enumerate(state):
        for a in A[1:]:
            S[a].append(i)
    
    starts = []
    for n in range(1, N+1):
        if len(S[n]) == 1:
            starts.append(n)
    
    for s in starts:
        R = [s]
        Used = [set() for _ in range(N+1)]
        ind = S[s][0]
        t = s
        for _ in range(N-3):
            for p in state[ind][1:]:
                Used[p].add(ind)
            for p in state[ind][1:]:
                if len(S[p]) - len(Used[p]) == 1:
                    t = p
                    break
            for nind in S[t]:
                if not nind in Used[t]:
                    ind = nind
            R.append(t)
        for p in state[ind][1:]:
            Used[p].add(ind)
        P = []
        for p in state[ind][1:]:
            if len(S[p]) - len(Used[p]) > 0:
                P.append((len(S[p])-len(Used[p]), p))
        P.sort(reverse=True)
        R.append(P[0][1])
        R.append(P[1][1])
        print(*R[::-1])
