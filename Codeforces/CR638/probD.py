import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    L = N.bit_length()-1
    ans = []
    if L == 1:
        ans = [N%2]
    else:
        for l in range(L-2):
            ans.append(2**l)
        if 3*2**(L-1)-1 <= N:
            ans.append(2**(L-2))
            ans.append(N-3*2**(L-1)+1)
        else:
            d = N - 2**L + 1
            ans.append(d//2)
            ans.append(d%2)
    print(L)
    print(*ans)