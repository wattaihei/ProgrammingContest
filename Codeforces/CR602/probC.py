import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    S = input().rstrip()
    Query.append((N, K, S))

for N, K, S in Query:
    state = list(S)
    exp = list("("*(N//2-K+1) + ")"*(N//2-K+1) + "()"*(K-1))
    ans = []
    for i in range(N):
        j = i
        while state[j] != exp[i]:
            j += 1
            if j == N: break
        ans.append((i+1, j+1))
        state[i] = exp[i]
        fill = "(" if exp[i] == ")" else ")"
        for ind in range(i+1, j+1):
            state[ind] = fill
    print(N)
    for l, r in ans:
        print(l, r)