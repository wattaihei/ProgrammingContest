Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    S = list(input())
    Query.append((N, K, S))

for N, K, S in Query:
    zeros = 0
    ans = []
    for i in range(N):
        if S[i] == '0':
            if i-zeros <= K:
                K -= (i-zeros)
                zeros += 1
            else:
                ans += ['0']*zeros
                ans += ['1']*(i-zeros-K)
                ans += ['0']
                ans += ['1']*K
                last = i
                break
    if not ans:
        ans = sorted(S)
    else:
        for i in range(last+1, N):
            ans.append(S[i])
    print("".join(ans))