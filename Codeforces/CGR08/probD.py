import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

L = 21
ans = [0]*N
for i in range(L):
    k = 0
    for a in A:
        if a&(1<<i):
            k += 1
    for j in range(k):
        ans[j] += (1<<i)

q = 0
for a in ans:
    q += a**2
print(q)