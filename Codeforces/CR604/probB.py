import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    dic = {}
    for i, a in enumerate(A):
        dic[a] = i
    l = N+1
    r = -1
    ans = ""
    for n in range(1, N+1):
        i = dic[n]
        l = min(l, i)
        r = max(r, i)
        if (r-l+1) == n:
            ans += "1"
        else:
            ans += "0"
    print(ans)