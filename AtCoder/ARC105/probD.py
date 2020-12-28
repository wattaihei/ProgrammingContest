import sys
input = sys.stdin.buffer.readline
from collections import Counter


def canWiFirst(N, A):
    if N%2 == 1:
        return False
    C = Counter(A)
    for c in C.values():
        if c%2 != 0:
            return True
    return False

Q = int(input())
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    
    print("First" if canWiFirst(N, A) else "Second")