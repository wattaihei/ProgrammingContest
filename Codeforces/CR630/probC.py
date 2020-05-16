import sys
input = sys.stdin.readline


Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    S = list(input().rstrip())
    Query.append((N, K, S))

for N, K, S in Query:
    ans = 0
    L = N//K
    for r in range(K):
        if K%2 == 0 and r >= K//2: break
        if K%2 == 1 and r == K//2:
            dic = {}
            for i in range(L):
                s = S[i*K+r]
                if s in dic:
                    dic[s] += 1
                else:
                    dic[s] = 1
            ans += L - max(list(dic.values()))
            break
        else:
            dic = {}
            for i in range(L):
                Ss = [S[i*K+r], S[i*K+(K-r-1)]]
                for s in Ss:
                    if s in dic:
                        dic[s] += 1
                    else:
                        dic[s] = 1
            ans += 2*L - max(list(dic.values()))
    print(ans)