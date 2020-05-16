import sys
input = sys.stdin.buffer.readline


def main():
    Q = int(input())
    Query = [None]*Q
    for i in range(Q):
        N = int(input())
        AB = [list(map(int, input().split())) for _ in range(N)]
        Query[i] = (N, AB)

    Pr = []
    for N, AB in Query:
        A, B = zip(*AB)
        B = B[N-1:] + B[:N-1]
        P = []
        S = 0
        for a, b in zip(A, B):
            p = 0
            if a-b > p:
                p = a-b
            P.append(p)
            S += p
        
        ans = 10**16
        for p, a in zip(P, A):
            t = a + S - p
            if t < ans:
                ans = t
        Pr.append(str(ans))
    print("\n".join(Pr))


if __name__ == "__main__":
    main()