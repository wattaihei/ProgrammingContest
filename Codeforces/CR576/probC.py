from bisect import bisect_right, bisect_left
from collections import Counter

def main():
    N, I = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()
    K = 2**(I*8//N)
    B = sorted(list(set(A)))
    bb = len(B)

    ans = N
    for i, l in enumerate(A):
        b = bisect_left(B, l)
        j = bisect_right(A, B[min(b+K-1, bb-1)])
        ans = min(N-(j-i), ans)
    print(ans)

if __name__ == "__main__":
    main()