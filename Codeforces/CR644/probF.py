import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    n, m = map(int, input().split())
    Ss = [list(input().rstrip()) for _ in range(n)]
    Query.append((n, m, Ss))

for N, M, Ss in Query:
    S1 = Ss.pop()
    ans = []
    for m in range(M):
        ok = True
        must = None
        for n in range(N-1):
            dif = 0
            for i in range(M):
                if i != m and Ss[n][i] != S1[i]:
                    dif += 1
            if dif > 1:
                ok = False
                break
            elif dif == 1:
                if not must is None and must != Ss[n][m]:
                    ok = False
                    break
                must = Ss[n][m]
        if ok:
            ans = S1
            if not must is None:
                ans[m] = must
            break
    if not ans:
        print(-1)
    else:
        print("".join(ans))