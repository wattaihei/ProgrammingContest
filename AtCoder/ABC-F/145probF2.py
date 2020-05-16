import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
A += [0, 0]

graph = [[] for _ in range(N+2)]
for i, a in enumerate(A):
    if i == N+1: break
    r = i+1
    while r != N+1 and A[r] >= a:
        r += 1
    l = i-1
    while l != -1 and A[l] > a:
        l -= 1
    if A[l] == a: graph[l].append((i, 0))
    else:
        if A[l] <= A[r]:
            graph[r].append((i, a-A[r]))
        elif A[l] > A[r]:
            graph[l].append((i, a-A[l]))


stack = [N]
Ind = [0]*(N+1)
dp = [[0] for _ in range(N+1)]
while stack:
    p = stack[-1]
    if Ind[p] == len(graph[p]):
        stack.pop()
        if len(graph[p]) == 0: continue
        elif len(graph[p]) == 1:
            ch, w = graph[p][0]
            P = dp[ch]
            if len(P) < K+1:
                dp[p] = P + [P[-1] + w]
            else:
                dp[p] = P[:]
        else:
            ch1, w1 = graph[p][0]
            ch2, w2 = graph[p][1]
            m = 0
            if len(dp[ch1]) < K+1:
                dp[ch1].append(dp[ch1][-1]+w1)
            if len(dp[ch2]) < K+1:
                dp[ch2].append(dp[ch2][-1]+w2)
            for k in range(1, min(K+1, len(dp[ch1])+len(dp[ch2])-1)):
                for i in range(k+1):
                    tmp = 0
                    if i < len(dp[ch1]):
                        tmp += dp[ch1][i]
                    if k-i < len(dp[ch2]):
                        tmp += dp[ch2][k-i]
                    m = max(m, tmp)
                dp[p].append(m)
    elif len(stack) > 1 and stack[-2] == graph[p][Ind[p]][0]:
        Ind[p] += 1
    else:
        stack.append(graph[p][Ind[p]][0])
        Ind[p] += 1

ans = 0
for i in range(N+1):
    for _, w in graph[i]:
        ans += w

ans -= dp[N][-1]
print(ans)