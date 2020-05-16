import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    l = 0
    r = M
    m = (l+r)//2
    while l < r:
        ok = True
        pre = 0
        for a in A:
            p = []
            if a <= pre <= a + m:
                continue
            elif pre < a:
                if (a + m) - M >= pre:
                    continue
                else:
                    pre = a
            else:
                ok = False
        if ok:
            if r == m:
                break
            r = m
            m = (l+r)//2
        else:
            if l == m:
                break
            l = m
            m = (l+r)//2
    print(r)


if __name__ == "__main__":
    main()