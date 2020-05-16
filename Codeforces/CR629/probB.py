import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for N, K in Query:
    a = 0
    for n in range(1, N+1):
        if a + n >= K:
            i1 = N - 1 - n
            i2 = N - (K-a)
            break
        a += n
    ans = ["a"]*N
    ans[i1] = "b"
    ans[i2] = "b"
    print("".join(ans))