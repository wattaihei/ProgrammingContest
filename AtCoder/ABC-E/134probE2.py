import heapq as hp

N = int(input())
A = [int(input()) for _ in range(N)]

q = []
for i, a in enumerate(A):
    print(a, q)
    if i==0:
        hp.heappush(q, -a)
        continue
    b = hp.heappop(q)
    if -a >= b:
        hp.heappush(q, b)
    hp.heappush(q, -a)
print(len(q))