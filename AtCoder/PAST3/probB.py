import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
Query = [list(map(int, input().split())) for _ in range(Q)]

Prob = [N]*M
Score = [set() for _ in range(N)]
for query in Query:
    if query[0] == 1:
        n = query[1]-1
        ans = 0
        for m in Score[n]:
            ans += Prob[m]
        print(ans)
    else:
        n, m = query[1]-1, query[2]-1
        Score[n].add(m)
        Prob[m] -= 1