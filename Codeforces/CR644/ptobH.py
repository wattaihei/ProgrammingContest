import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, M = map(int, input().split())
    Ss = [input().rstrip() for _ in range(N)]
    Query.append((N, M, Ss))

for N, M, Ss in Query:
    border = ((1<<M)-N)//2
    r = (1<<M)-1
    l = 0
    while r - l > 1:
        m = (r+l)//2
        # T = "0"*(M-m.bit_length()) + bin(m)[2:]
        seq = m
        for S in Ss:
            if int(S, 2) < m:
                seq -= 1
        if seq <= border:
            l = m
        else:
            r = m
    print("0"*(M-r.bit_length()) + bin(r)[2:])