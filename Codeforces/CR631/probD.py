import sys
input = sys.stdin.readline



Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for D, mod in Query:
    L = D.bit_length()
    A = []
    for i in range(L-1):
        A.append(1<<i)
    A.append(D-(1<<(L-1))+1)
    ans = 1
    for a in A:
        ans = (ans * (a+1)) % mod
    print((ans-1)%mod)