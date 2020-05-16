import sys
input = sys.stdin.readline

from bisect import bisect_left

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    dic = {}
    for i, a in enumerate(A):
        if a in dic:
            dic[a].append(i)
        else:
            dic[a] = [i]
    
    Ns = list(dic.keys())

    ans = 0
    for a, A1 in dic.items():
        ans = max(ans, len(A1))
        for b, B1 in dic.items():
            if a == b: continue
            l1 = 0; r1 = len(A1)-1
            l2 = 0; r2 = len(B1)-1
            while l1 < r1:
                while l2 <= len(B1)-1 and B1[l2] < A1[l1]:
                    l2 += 1
                while r2 >= 0 and B1[r2] > A1[r1]:
                    r2 -= 1
                t = (l1+1)*2+(r2-l2+1)
                if t > ans:
                    ans = t
                l1 += 1
                r1 -= 1
    print(ans)
