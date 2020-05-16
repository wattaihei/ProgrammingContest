import sys
input = sys.stdin.readline

INF = 10**15

Q = int(input())

Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    ans = INF
    dic = {}
    for i, a in enumerate(A):
        if a in dic:
            ans = min(ans, i-dic[a]+1)
            dic[a] = i
        else:
            dic[a] = i
    if ans == INF:
        ans = -1
    print(ans)