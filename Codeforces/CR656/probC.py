import sys
input = sys.stdin.readline


Q = int(input())
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        ans = 0
    else:
        pre = A[-2]
        ans = N-2
        up = A[-1] <= A[-2]
        for a in reversed(A[:-2]):
            if up:
                if a < pre:
                    up = False
            else:
                if a > pre:
                    break
            pre = a
            ans -= 1
    print(ans)
