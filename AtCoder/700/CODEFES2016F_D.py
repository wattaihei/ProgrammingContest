import sys
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())
X = list(map(int, input().split()))


def main():
    P = [[] for _ in range(M)]

    for x in X:
        P[x%M].append(x)

    ans = 0
    checked = [False]*M
    for m in range(M):
        if checked[m]:
            continue
        if m == 0 or m == M-m:
            ans += len(P[m])//2
        else:
            P1, P2 = P[m], P[M-m]
            L1, L2 = len(P[m]), len(P[M-m])
            if L2 > L1:
                P1, P2 = P[M-m], P[m]
                L1, L2 = len(P1), len(P2)
            
            C1 = Counter(P1)
            n = 0
            for num, c1 in C1.items():
                n += c1//2
            if L1 - n*2 <= L2:
                ans += (L1+L2)//2
            else:
                ans += L2 + n

            checked[m] = True
            checked[M-m] = True

    print(ans)


if __name__ == "__main__":
    main()