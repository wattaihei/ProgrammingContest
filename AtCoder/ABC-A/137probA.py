import sys
input = sys.stdin.readline

A, B = map(int, input().split())
print(max(A+B, A-B, A*B))