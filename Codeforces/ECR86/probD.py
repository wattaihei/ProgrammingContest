import sys
input = sys.stdin.readline
import heapq as hp

N, K = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
q = []
ans = []
for a in A:
    if q:
        num, ind = hp.heappop(q)
        if num < C[a-1]:
            ans[ind].append(a)
            num += 1
            hp.heappush(q, (num, ind))
        else:
            ans.append([a])
            hp.heappush(q, (1, len(ans)-1))
    else:
        ans.append([a])
        hp.heappush(q, (1, len(ans)-1))

print(len(ans))
for A in ans:
    print(len(A), *A)