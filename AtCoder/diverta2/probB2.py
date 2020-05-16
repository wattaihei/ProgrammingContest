from operator import itemgetter
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

A1 = sorted(A, key=itemgetter(0))
P = []
pre = 0
for x1, y1 in A1:
    P.append(x1 - pre)
    pre = x1

A2 = sorted(A, key=itemgetter(1))
Q = []
pre = 0
for x2, y2 in A2:
    Q.append(y2 - pre)
    pre = y2

ans = N
for p in P:
    for q in Q:
        a = 0
        for i in range(N):
            xi, yi = A[i]
            for j in range(N):
                if j == i:
                    continue
                xj, yj = A[j]
                if xj - xi == p and yj - yi == q:
                    a += 1
        #print(p, q, a)
        ans = min(N-a, ans)
    
print(ans)