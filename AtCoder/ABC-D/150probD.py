from fractions import gcd

import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    B = []

    ok = True
    a = A[0]
    c = 0
    while a%2 == 0:
        a //= 2
        c += 1
    
    p = 2**c

    for a in A:
        if a % p == 0 and a % (2*p) != 0:
            B.append(a//p)
        else:
            ok = False
            break
    if not ok:
        print(0)
    else:
        B.sort()
        g = 1
        for b in B:
            l = gcd(b, g)
            g = g*b//l
            if g > M:
                ok = False
                break
        if not ok:
            print(0)
        else:
            p = g*2**(c-1)
            ans = (M+p)//(2*p)
            print(ans)


if __name__ == "__main__":
    main()