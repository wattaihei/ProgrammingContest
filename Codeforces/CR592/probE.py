import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

afA = [0]*(N+1)
for i in reversed(range(N)):
    afA[i] = afA[i+1] + A[i]

prA = [0]*(N+1)
for i in range(N):
    prA[i+1] = prA[i] + A[i]

l = 0
r = 10**10
while r-l > 1:
    delta = (l+r)//2
    
    fw = 0
    ok = False
    for bf in range(N):
        while fw < N and A[bf] + delta >= A[fw]:
            fw += 1
        score = A[i]*bf - prA[bf]
        if fw != N:
            score += A[fw]*(N-fw) - afA[fw]
        if score <= K:
            ok = True
            break
    print(delta, ok)
    if ok:
        r = delta
    else:
        l = delta

print(l)