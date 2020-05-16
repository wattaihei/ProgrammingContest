import sys
input = sys.stdin.readline

from bisect import bisect_left

N, K = map(int, input().split())
A = list(map(int, input().split()))

indexes = {}
for i, a in enumerate(A):
    if not a in indexes.keys():
        indexes[a] = [i]
    else:
        indexes[a].append(i)

L = [N]
ind = N
while True:
    ind = (ind+1)%(N+1)
    if ind == N: break
    a = A[ind]
    if indexes[a][-1] == ind:
        ind = indexes[a][0]
        L.append(ind)
    else:
        loc = bisect_left(indexes[a], ind)
        ind = indexes[a][loc+1]
    

start_ind = L[(K-1)%len(L)] + 1
if start_ind == N+1: start_ind = 0
in_list = {}
for a in A:
    in_list[a] = 0
ans = []
for i in range(start_ind, N):
    a = A[i]
    if in_list[a] == 0:
        ans.append(a)
        in_list[a] = 1
    else:
        while True:
            b = ans.pop()
            in_list[b] -= 1
            if a == b:
                break

for a in ans:
    print(a, end=' ')
print()
