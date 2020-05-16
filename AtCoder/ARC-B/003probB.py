import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    S = input().rstrip()[::-1]
    A.append(S)

A.sort()
for a in A:
    print(a[::-1])