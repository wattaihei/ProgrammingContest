N = int(input())
C = input()

ABXY = ['A', 'B', 'X', 'Y']
probs = []

def dfs(L):
    if len(L) == 4: 
        probs.append(L)
        return
    for a in ABXY:
        dfs(L+[a])

dfs([])
ans = N
for L in probs:
    a1 = ''.join(L[:2])
    a2 = ''.join(L[2:])
    A = [a1, a2]
    pa = False
    count = 0
    for i in range(N):
        if pa:
            pa = False
            continue
        count += 1
        if i == N-1: break
        if C[i:i+2] in A:
            pa = True
    ans = min(ans, count)

print(ans)