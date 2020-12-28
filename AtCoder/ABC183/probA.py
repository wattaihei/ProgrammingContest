import sys
input = sys.stdin.buffer.readline

N = int(input())
print(N if N >= 0 else 0)