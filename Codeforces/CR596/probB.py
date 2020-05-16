import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, K, D, A))

for N, K, D, A in Query:
    dic = {}
    for i in range(D):
        if not A[i] in dic.keys():
            dic[A[i]] = 1
        else:
            dic[A[i]] += 1
    ans = len(dic)
    now = ans
    for i in range(D, N):
        if not A[i] in dic.keys():
            now += 1
            dic[A[i]] = 1
        else:
            if dic[A[i]] == 0:
                now += 1
            dic[A[i]] += 1
        dic[A[i-D]] -= 1
        if dic[A[i-D]] == 0:
            now -= 1
        ans = min(ans, now)
    print(ans)