import sys
input = sys.stdin.readline
import math

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for n, k in Query:
    ans = 10**18
    for a in range(1, int(math.sqrt(n)+2)):
        if n % a == 0:
            if n//a <= k:
                ans = min(ans, a)
            if a <= k:
                ans = min(ans, n//a)
    print(ans)