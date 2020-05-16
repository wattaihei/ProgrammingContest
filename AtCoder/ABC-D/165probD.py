import sys
input = sys.stdin.readline

A, B, N = map(int, input().split())

if N >= B:
    x = B-1
else:
    x = N

print(A*x//B)