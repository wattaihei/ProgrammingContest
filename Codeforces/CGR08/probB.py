import sys
input = sys.stdin.readline

N = int(input())
Ss = list("codeforces")

L = len(Ss)

n = 1
while pow(n, L) < N:
    n += 1

ind = -1
for i in range(L):
    if pow(n, L-i)*pow(n-1, i) >= N:
        ind = i

ans = ""
for i, s in enumerate(Ss):
    if i <= ind-1:
        ans += s*(n-1)
    else:
        ans += s*n
print(ans)