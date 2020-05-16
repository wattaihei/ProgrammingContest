import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

Seq = [-1]*(N+1)
Seq[1] = 0
now = 1
while True:
    n = A[now]
    if Seq[n] == -1:
        Seq[n] = Seq[now] + 1
        now = n
    else:
        cycle = Seq[now] + 1 - Seq[n]
        now = n
        break

if Seq[now] > K:
    for n in range(N+1):
        if Seq[n] == K:
            print(n)
            break
else:
    rem = (K-Seq[now])%cycle
    for _ in range(rem):
        now = A[now]
    print(now)