import sys
input = sys.stdin.buffer.readline

mod = 10**9 + 7
Q = int(input())
for _ in range(Q):
    N, A, B = map(int, input().split())
    C = N-A-B
    if C < 0:
        ans = 0
    else:
        q = (N-A+1)*(N-B+1)
        p = (C+1)*(C+2)
        ans = (2*(q-p)*p + p**2) % mod
    print(ans)