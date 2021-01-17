
if __name__ == "__main__":
        
    import sys
    input = sys.stdin.buffer.readline

    INF = 10**18

    N, M = map(int, input().rstrip().split())
    Connected = [[False]*N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        Connected[a-1][b-1] = True
        Connected[b-1][a-1] = True

    B = [set() for _ in range(N+1)]
    for bit in range(1<<N):
        ok = True
        for i in range(N):
            if (1<<i)&bit:
                for j in range(i+1, N):
                    if (1<<j)&bit:
                        if not Connected[i][j]:
                            ok = False
                            break
        if ok:
            c = bin(bit).count("1")
            B[c].add(bit)

    for c in range(2, N+1):
        for bit in B[c]:
            for n in range(N):
                if (1<<n)&bit:
                    nbit = bit ^ (1<<n)
                    if nbit in B[c-1]:
                        B[c-1].remove(nbit)

    active = []
    for c in range(N+1):
        for bit in B[c]:
            active.append(bit)

    dp = [INF]*(1<<N)
    dp[0] = 0
    for bit in range(1<<N):
        for nbit in active:
            dp[bit|nbit] = min(dp[bit|nbit], dp[bit]+1)

    print(dp[-1])