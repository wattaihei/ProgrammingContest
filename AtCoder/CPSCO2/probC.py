import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = input().rstrip()

A = []
a = 0
for s in S:
    if s == "(":
        a += 1
    else:
        a -= 1
    A.append(a)

A.sort(reverse=True)
ans = 0
for i in range(K):
    ans += A[i]

print(ans)