import sys
input = sys.stdin.readline
import heapq as hp

N = int(input())
A = list(map(int, input().split()))

dic = {}
canuse = [True]*(N+2)
for i, a in enumerate(A):
    dic[a] = i
    canuse[a] = False

q = []
for i in range(N+1):
    if canuse[i]:
        hp.heappush(q, i)

ans = []
for i, a in enumerate(A):
    b = hp.heappop(q)
    ans.append(str(b))
    if dic[a] == i:
        hp.heappush(q, a)

print(" ".join(ans))