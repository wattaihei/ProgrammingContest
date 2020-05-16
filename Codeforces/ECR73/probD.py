import heapq as hp

Q = int(input())
data = []
for _ in range(Q):
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    data.append([N, A, B])

for N, A, B in data:
    if N == 1:
        print(0)
        continue
    Pair = [-1]*N
    q = []
    for i in range(N):
        if i == 0:
            pre = A[i]
            continue
        if pre == A[i]:
            Pair[i] = pre
            hp.heappush(q, (pre, i))
        pre = A[i]
    ans = 0
    while q:
        (a, i) = hp.heappop(q)
        if Pair[i] == -1:
            continue
        
        if B[i] < B[i-1]:
            ans += B[i]
            A[i] += 1
            if i < N-1:
                if A[i+1] == A[i]:
                    Pair[i+1] = A[i]
                    hp.heappush(q, (A[i], i+1))
                else:
                    Pair[i+1] = -1
        elif B[i] > B[i-1]:
            ans += B[i-1]
            A[i-1] += 1
            if i > 1:
                if A[i-1] == A[i-2]:
                    Pair[i-1] = A[i-1]
                    hp.heappush(q, (A[i-1], i-1))
                else:
                    Pair[i-1] = -1
        else:
            
        Pair[i] = -1
    print(ans)
