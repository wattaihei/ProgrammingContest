import sys
input = sys.stdin.readline


L = 2019
S = input().rstrip()


A = {0 : 1}
ans = 0
tmp = 0
c = 1
for s in S[::-1]:
    n = int(s)
    tmp = (tmp + c*n) % L
    c = c * 10 % L
    if tmp in A:
        A[tmp] += 1
    else:
        A[tmp] = 1

for v in A.values():
    ans += v*(v-1)//2
print(ans)