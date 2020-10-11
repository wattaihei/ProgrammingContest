from math import gcd

import sys
input = sys.stdin.buffer.readline

def main():
    Q = int(input())
    for _ in range(Q):
        N = int(input())
        A = list(map(int, input().split()))
        gmax = 0
        p = -1
        for i, a in enumerate(A):
            if a > gmax:
                gmax = a
                p = i
        
        ans = [str(A[p])]
        remain = set(range(N))
        remain.remove(p)
        nowg = A[p]
        while len(remain) > 0:
            gmax = 0
            np = -1
            for r in remain:
                g = gcd(A[r], nowg)
                if g > gmax:
                    gmax = g
                    np = r
            remain.remove(np)
            ans.append(str(A[np]))
            nowg = gcd(A[np], nowg)
        
        print(" ".join(ans))
    
if __name__ == "__main__":
    main()