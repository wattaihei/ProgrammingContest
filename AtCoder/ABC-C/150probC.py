N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

W = []

def dfs(checked, L):
    if len(L) == N:
        W.append(L)
        return
    for i in range(1, N+1):
        if not checked[i]:
            checked[i] = True
            dfs(checked, L+[i])
            checked[i] = False
    return

dfs([False]*(N+1), [])


for i, L in enumerate(W):
    if L == P:
        ip = i
    if L == Q:
        iq = i

print(abs(ip-iq))