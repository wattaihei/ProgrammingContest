import sys
input = sys.stdin.buffer.readline
from bisect import bisect_left


N, T = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

A1 = A[:N//2]
A2 = A[N//2:]

for bit in range(1<<(N//2)):
    
    for i in range(N//2):
        if bit&(1<<i):
