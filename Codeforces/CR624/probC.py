import sys
input = sys.stdin.readline

Alp = [chr(i) for i in range(97, 97+26)]

Q = int(input())
Query = []
for _ in range(Q):
    N, M = map(int, input().split())
    S = list(input().rstrip())
    A = list(map(int, input().split()))
    Query.append((N, M, S, A))

for N, M, S, A in Query:
    dic = {}
    ans = {}
    for a in Alp:
        dic[a] = [0]
        ans[a] = 0
    
    for s in S:
        for a in Alp:
            if a == s:
                dic[a].append(dic[a][-1]+1)
            else:
                dic[a].append(dic[a][-1])
    
    A.append(N)
    for n in A:
        for a in Alp:
            ans[a] += dic[a][n]
    
    for a in Alp:
        print(ans[a], end=" ")
    print()