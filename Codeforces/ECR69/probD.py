N, M, K = map(int, input().split())
A = list(map(int, input().split()))

B = [A[0]]
for i in range(1, N):
    B.append(B[-1]+A[i])

L = [((i+1)//m)*K for i in range(N)]

l = 0
r = 0
ans = 0
while True:
    if 
