import sys
input = sys.stdin.readline
from math import gcd

N = int(input())
graph = [[] for _ in range(N)]
Par = [-1]*N
PQ = []
for i in range(N):
    p, q, l, r = map(int, input().split())
    PQ.append((p, q))
    graph[i] = (l-1, r-1)
    if l != 0:
        Par[l-1] = i
    if r != 0:
        Par[r-1] = i

root = -1
for n in range(N):
    if Par[n] == -1:
        root = n
        break


stack = [root]
W = [-1]*N
while stack:
    p = stack.pop()
    if p >= 0:
        stack.append(~p)
        for n in graph[p]:
            if n != -1:
                stack.append(n)
    else:
        p = ~p
        l, r = graph[p]
        a, b = PQ[p]
        if l == -1 and r == -1:
            g = gcd(a, b)
            W[p] = (a + b) // g
        else:
            if l == -1:
                wr = W[r]
                wl = 1
            elif r == -1:
                wl = W[l]
                wr = 1
            else:
                wl = W[l]; wr = W[r]
            c, d = wl*a, wr*b
            g = gcd(c, d)
            W[p] = c//g * wr + d//g * wl
        
print(W[root])