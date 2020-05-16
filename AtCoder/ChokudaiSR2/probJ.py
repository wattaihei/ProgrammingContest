import sys
input = sys.stdin.readline
from math import sqrt

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    L = int(1E12)
    for i, (a, b) in enumerate(AB):
        if max(a, b) < L:
            L = max(a, b)
            mi = i

    ma, mb = AB[mi]

    probs = set()
    for i in range(1, int(sqrt(ma))+1):
        if ma%i == 0:
            probs.add(i)
            probs.add(ma//i)

    for i in range(1, int(sqrt(mb))+1):
        if mb%i == 0:
            probs.add(i)
            probs.add(mb//i)

    P = list(probs)
    P.sort(reverse=True)
    ans = 1
    for p in P:
        ok = True
        for i, (a, b) in enumerate(AB):
            if i == mi:
                continue
            if a%p != 0 and b%p != 0:
                ok = False
                break
        if ok:
            ans = p
            break

    print(ans)

if __name__ == "__main__":
    main()