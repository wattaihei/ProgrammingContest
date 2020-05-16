class BIT():
    def __init__(self, max_X):
        self.max_X = max_X + 1
        self.bit = [10**15]*(self.max_X+1)

    def update(self, x, a):
        while x <= self.max_X:
            if a < self.bit[x]:
                self.bit[x] = a
            x += x & -x

    def query_min(self, x):
        s = 10**14
        while x > 0:
            if self.bit[x] < s:
                s = self.bit[x]
            x -= x & -x
        return s

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

offset = (N+1)//2
All = offset*2

BITodd = BIT(offset)
BITeven = BIT(offset)

B = [0]
for i, a in enumerate(A):
    B.append(a)
    i += 1
    if i%2 == 1:
        BITodd.update((i+1)//2, a)
    else:
        BITeven.update(i//2, a)

minus_odd = 0
minus_even = 0
ans = 0
for query in Query:
    if query[0] == 1:
        x, a = query[1], query[2]
        if x%2 == 0:
            now_a = B[x] - minus_even
            if now_a >= a:
                BITeven.update((x+1)//2, B[x]-a)
                ans += a
                B[x] -= a
        else:
            now_a = B[x] - minus_odd
            if now_a >= a:
                BITodd.update((x+1)//2, B[x]-a)
                ans += a
                B[x] -= a
    elif query[0] == 2:
        a = query[1]
        min_odd = BITodd.query_min(offset) - minus_odd
        if min_odd >= a:
            minus_odd += a
            ans += a*((N+1)//2)
    else:
        a = query[1]
        min_even = BITeven.query_min(offset) - minus_even
        min_odd = BITodd.query_min(offset) - minus_odd
        if min(min_even, min_odd) >= a:
            minus_odd += a
            minus_even += a
            ans += a*N

print(ans)
