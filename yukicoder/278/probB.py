import sys
input = sys.stdin.buffer.readline

mod = 10**9+7
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().rstrip().split()))

    ans = 1
    for a in A:
        ans *= (a+1)
        ans %= mod

    ans = (ans-1)%mod
    print(ans)