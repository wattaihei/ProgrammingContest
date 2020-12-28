import sys
input = sys.stdin.buffer.readline
from math import sqrt

S, P = map(int, input().rstrip().split())

def solve():
    for n in range(1, int(sqrt(P))+2):
        if P%n == 0:
            m = P//n
            if m+n == S:
                return True
    return False

print("Yes" if solve() else "No")