from collections import Counter

Q = int(input())
data = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    data.append([N, A])

for N, A in data:
    ans = 'YES'
    B = Counter(A)
    C = []
    for k, v in B.items():
        if v % 2 != 0:
            ans = 'NO'
            break
        C.extend([k]*(v//2))
    if ans == 'YES':
        C.sort()
        for k in range(N):
            if k == 0:
                a = C[k]*C[2*N-k-1]
            else:
                if C[k]*C[2*N-k-1] != a:
                    ans = 'NO'
                    break
    print(ans)
