import sys
input = sys.stdin.readline

A = set(map(int, input().split()))

print("Yes" if len(A) == 2 else "No")