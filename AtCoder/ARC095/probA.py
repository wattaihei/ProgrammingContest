import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().rstrip().split()))

B = []
for i, a in enumerate(A):
    B.append((a, i))

B.sort()


a1 = B[N//2-1][0]
a2 = B[N//2][0]

ans = [-1]*N
for a, i in B[:N//2]:
    ans[i] = a2

for a, i in B[N//2:]:
    ans[i] = a1

print(*ans, sep="\n")