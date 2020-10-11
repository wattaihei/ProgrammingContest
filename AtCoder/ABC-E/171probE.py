import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

X = 0
for a in A:
    X ^= a

ans = []
for a in A:
    ans.append(X^a)

print(*ans)