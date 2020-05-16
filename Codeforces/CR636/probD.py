import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, K, A))

for N, K, A in Query:
    MIN = []
    MAX = []
    dic = {}
    for n in range(N//2):
        a1 = A[n]; a2 = A[-1-n]
        MIN.append(min(a1+1, a2+1))
        MAX.append(max(a1+K, a2+K))
        p = a1 + a2
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    
    MIN.sort()
    MAX.sort()
        
    ans = 10**14
    for k in range(2, 2*K+1):
        small_than_k = bisect_left(MAX, k)
        large_than_k = N//2 - bisect_right(MIN, k)
        two = small_than_k + large_than_k
        zero = dic[k] if k in dic else 0
        one = N//2 - two - zero
        ans = min(ans, two*2+one)
    print(ans)