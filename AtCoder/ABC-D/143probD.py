import sys
input = sys.stdin.readline

from bisect import bisect_left

N = int(input())
L = list(map(int, input().split()))

ans = 0
L.sort()
for i in range(N-2):
    for j in range(i+1, N-1):
        k = bisect_left(L, L[i]+L[j])
        ans += k - j - 1
print(ans)