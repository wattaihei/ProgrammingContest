import sys
input = sys.stdin.readline


Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    ok = True
    tmp = 0
    used = [False]*(N+1)
    now = 1
    ans = []
    for a in A:
        if tmp < a:
            ans.append(a)
            used[a] = True
            tmp = a
        else:
            while used[now]:
                now += 1
            if now > tmp:
                ok = False
                break
            ans.append(now)
            used[now] = True
    if not ok:
        print(-1)
    else:
        print(*ans)
    