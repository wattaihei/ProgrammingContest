mod = 10**9+7


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline

    N, M = map(int, input().rstrip().split())
    A = list(map(int, input().rstrip().split()))

    ans = 1
    S = sum(A) + N
    for i in range(1, S+1):
        ans = ans * (N+M-i+1) * pow(i, mod-2, mod) % mod
    print(ans)