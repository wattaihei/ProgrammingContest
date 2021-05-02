import sys
input = sys.stdin.readline

Q = int(input())

Query = []
for _ in range(Q):
    N = int(input())
    state = [list(map(int, input().split())) for _ in range(N)]
    Query.append((N, state))

for ind, (N, state) in enumerate(Query):

    ans1 = 0
    for i in range(N):
        ans1 += state[i][i]
    
    ans2 = 0
    for r in range(N):
        ok = True
        S = set()
        for h in range(N):
            p = state[r][h]
            if p in S:
                ok = False
                break
            S.add(p)
        if not ok:
            ans2 += 1
    
    ans3 = 0
    for h in range(N):
        ok = True
        S = set()
        for r in range(N):
            p = state[r][h]
            if p in S:
                ok = False
                break
            S.add(p)
        if not ok:
            ans3 += 1



    print("Case #{}:".format(ind+1), ans1, ans2, ans3)