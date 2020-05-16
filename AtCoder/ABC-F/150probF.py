import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

h = 10**11+7
b = 10**7+7

H = [1]
for _ in range(N):
    H.append((H[-1]*b)%h)

allSum = 0
for i in range(N):
    allSum = (allSum + H[i]) % h

ok = [True]*N
ans = [0]*N

L = 30
for l in range(L):
    HashA = 0
    for i, a in enumerate(A):
        if (1<<l)&a:
            HashA = (HashA + H[i]) % h

    HashB = 0
    for i, a in enumerate(B):
        if (1<<l)&a:
            HashB = (HashB + H[i]) % h
    
    for k in range(N):
        if (HashA+HashB)%h == allSum:
            ans[k] += (1<<l)
        elif HashA != HashB:
            ok[k] = False
        HashB = (HashB * b) % h
        if (1<<l)&B[-k-1]:
            HashB = (HashB + h - H[N] + 1) % h

for k in range(N):
    if ok[k]:
        print(k, ans[k])