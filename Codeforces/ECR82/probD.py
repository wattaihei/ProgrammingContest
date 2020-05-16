import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, M, A))

for N, M, A in Query:
    delta = sum(A)-N
    if delta < 0:
        print(-1)
    else:
        L = max(N, max(A)).bit_length()
        D = [0]*L
        for a in A:
            D[a.bit_length()-1] += 1
        
        S = 0
        to = -1
        ans = 0
        for l in range(L):
            if to != -1 and D[l] > 0:
                ans += (l-to)
                to = -1
                D[l] -= 1
            S += D[l]*(1<<l)
            if (1<<l)&N:
                if S >= (1<<l):
                    S -= (1<<l)
                elif to == -1:
                    to = l
        if to != -1:
            print(-1)
        else:
            print(ans)