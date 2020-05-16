import sys
input = sys.stdin.buffer.readline
from bisect import bisect_left

Q = int(input())
Query = []
for _ in range(Q):
    n1, n2, n3 = map(int, input().split())
    A1 = list(map(int, input().split()))
    A2 = list(set(map(int, input().split())))
    A3 = list(set(map(int, input().split())))
    Query.append((n1, n2, n3, A1, A2, A3))

for n1, n2, n3, A1, A2, A3 in Query:
    n2 = len(A2)
    n3 = len(A3)
    A2.sort()
    A3.sort()
    ans = 10**60
    for a in A1:
        i2 = bisect_left(A2, a)
        B2 = []
        if i2 < n2:
            B2.append(A2[i2])
        if i2 < n2-1:
            B2.append(A2[i2+1])
        if i2 > 0:
            B2.append(A2[i2-1])
        
        for b2 in B2:
            i3 = bisect_left(A3, (a+b2+1)//2)
            B3 = []
            if i3 < n3:
                B3.append(A3[i3])
            if i3 < n3 - 1:
                B3.append(A3[i3+1])
            if i3 > 0:
                B3.append(A3[i3-1])
            for b3 in B3:
                s = (a-b2)**2 + (b2-b3)**2 + (b3-a)**2
                if s < ans:
                    ans = s
        
        i3 = bisect_left(A3, a)
        B3 = []
        if i3 < n3:
            B3.append(A3[i3])
        if i3 < n3-1:
            B3.append(A3[i3+1])
        if i3 > 0:
            B3.append(A3[i3-1])
        
        for b3 in B3:
            i2 = bisect_left(A2, (a+b3+1)//2)
            B2 = []
            if i2 < n2:
                B2.append(A2[i2])
            if i2 < n2 - 1:
                B2.append(A2[i2+1])
            if i2 > 0:
                B2.append(A2[i2-1])
            for b2 in B2:
                s = (a-b2)**2 + (b2-b3)**2 + (b3-a)**2
                if s < ans:
                    ans = s
    print(ans)
