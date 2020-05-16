import sys
input = sys.stdin.readline


Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    if len(set(A)) == 1:
        la = 1
        ans = ["1"]*N
    else:
        if N%2 == 0:
            la = 2
            ans = [str(i%2+1) for i in range(N)]
        else:
            ind = -1
            for i in range(N):
                if A[i-1] == A[i]:
                    ind = i
            if ind == -1:
                la = 3
                ans = [str(i%2+1) for i in range(N)]
                ans[-1] = "3"
            else:
                la = 2
                ans = [str(i%2+1) if i < ind else str((i+1)%2+1) for i in range(N)]
    print(la)
    print(" ".join(ans))