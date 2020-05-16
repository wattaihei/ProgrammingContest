import sys

def solve():
    N = int(input())
    D = 0
    for n in range(2, N+1):
        print("? {0} {1}".format(1, n))
        sys.stdout.flush()
        d = int(input())
        if d > D:
            D = d
            p = n
    ans = 0
    for n in range(1, N+1):
        if n == p: continue
        print("? {0} {1}".format(p, n))
        sys.stdout.flush()
        d = int(input())
        ans = max(ans, d)
    print("! {0}".format(ans))

if __name__ == "__main__":
    solve()