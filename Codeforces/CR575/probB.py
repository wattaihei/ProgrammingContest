q = int(input())
Q = []
for _ in range(q):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Q.append([N, K, A])

for q in Q:
    N, K, A = q
    odd = []
    for i, a in enumerate(A):
        if a % 2 != 0:
            odd.append(i+1)
    od = len(odd)
    if od < K or (od - K)%2 != 0:
        print('No')
        continue
    ans = odd[:K-1]
    ans.append(N)
    print('Yes')
    print(' '.join([str(a) for a in ans]))