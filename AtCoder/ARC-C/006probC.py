from bisect import bisect_left

N = int(input())
A = [int(input()) for _ in range(N)]

q = []
for a in A:
    i = bisect_left(q, a)
    if i == len(q):
        q.append(a)
    else:
        q.pop(i)
        q.append(a)
        q.sort()
print(len(q))