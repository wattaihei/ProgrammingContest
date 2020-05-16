import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

print(max(0, C+B-A))