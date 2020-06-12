import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = [-1]*(2**N)
T = [i for i in range(2**N)]
for n in range(N):
    New = []
    for i in range(2**(N-n-1)):
        t1, t2 = T[2*i], T[2*i+1]
        if A[t1] > A[t2]:
            ans[t2] = n+1
            New.append(t1)
        else:
            ans[t1] = n+1
            New.append(t2)
    T = New[:]

ans[New[0]] = N
print(*ans, sep="\n")