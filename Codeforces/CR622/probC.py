import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

sta1 = []
dp1 = [0]*(N+1)
for i, a in enumerate(A):
    count = 0
    mustscore = dp1[i]
    while sta1 and sta1[-1][0] > a:
        s, num = sta1.pop()
        count += num
        mustscore += (s-a)*num
    dp1[i+1] = mustscore
    sta1.append((a, count+1))

sta2 = []
dp2 = [0]*(N+1)
for i in reversed(range(N)):
    a = A[i]
    count = 0
    mustscore = dp2[i+1]
    while sta2 and sta2[-1][0] > a:
        s, num = sta2.pop()
        count += num
        mustscore += (s-a)*num
    dp2[i] = mustscore
    sta2.append((a, count+1))

PA = 10**17
ind = -1
for n in range(N):
    p = dp1[n+1] + dp2[n]
    if p < PA:
        PA = p
        ind = n

ans = A[:]
for i in range(ind+1, N):
    A[i] = min(A[i-1], A[i])
for i in reversed(range(ind)):
    A[i] = min(A[i], A[i+1])

print(*A)