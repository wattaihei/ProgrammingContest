import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = [0]*N
for i, a in enumerate(A):
    ans[a-1] += 1

print(*ans, sep="\n")