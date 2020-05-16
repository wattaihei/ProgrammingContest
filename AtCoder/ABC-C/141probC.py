N, K, Q = map(int, input().split())

A = [0 for _ in range(N)]

for _ in range(Q):
    a = int(input())
    A[a-1] += 1

for i in range(N):
    if A[i] > Q-K:
        print('Yes')
    else:
        print('No')