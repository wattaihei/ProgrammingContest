N = int(input())

K = -1
for k in range(N+1):
    if k*(k-1)//2 == N:
        K = k
        break
    elif k*(k-1)//2 > N:
        break

if N == 1:
    print('Yes')
    print(2)
    print(1, 1)
    print(1, 1)
elif K == -1:
    print('No')
else:
    print('Yes')
    print(K)
    n = 0
    S = [[] for _ in range(K)]
    for i in range(K):
        for j in range(i+1, K):
            n += 1
            S[i].append(n)
            S[j].append(n)
    for s in S:
        print(len(s), ' '.join([str(a) for a in s]))