import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))

c = 0
for a in A:
    if a%2 == 0:
        c += 1
print(min(c, N-c))