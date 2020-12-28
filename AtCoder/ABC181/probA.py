import sys
input = sys.stdin.buffer.readline

N = int(input())
print("White" if N%2 == 0 else "Black")