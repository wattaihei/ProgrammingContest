import sys
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    M = max(A)
    scores = [[] for _ in range(M+1)]

    for a in A:
        c = 0
        while a > 0:
            scores[a].append(c)
            a //= 2
            c += 1
        scores[0].append(c)

    for a, L in enumerate(scores):
        if len(L) < K: continue
        L.sort()
        if a == 0:
            ans = sum(L[:K])
        else:
            ans = min(ans, sum(L[:K]))

    print(ans)

if __name__ == "__main__":
    main()