import sys
input = sys.stdin.buffer.readline
T = int(input())
for _ in range(T):
    N = int(input())
    while N%2 == 0:
        N //= 2
    while N%5 == 0:
        N //= 5
    
    
