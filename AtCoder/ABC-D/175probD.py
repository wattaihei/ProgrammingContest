import sys
input = sys.stdin.buffer.readline
INF = 10**18

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = -INF
    for start in range(N):
        T = K
        S = {start: 0}
        seq = {start: 0}
        t = start
        while T > 0 and not P[t]-1 in S:
            seq[P[t]-1] = seq[t] + 1
            S[P[t]-1] = S[t] + C[P[t]-1]
            ans = max(ans, S[P[t]-1])
            t = P[t] - 1
            T -= 1
        if T > 0:
            scoredelta = S[t] + C[P[t]-1] - S[P[t]-1]
            cycle = seq[t] + 1 - seq[P[t] - 1]
            score = S[P[t]-1]
            T += cycle - 1
            count = T // cycle - 1
            T -= count * cycle
            score += count * scoredelta
            ans = max(ans, score)
            t = P[t]-1
            while T > 0:
                score += C[t]
                ans = max(ans, score)
                t = P[t]-1
                T -= 1
    print(ans)

if __name__ == "__main__":
    main()