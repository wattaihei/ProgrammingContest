import sys
input = sys.stdin.readline

n, w = map(int, input().rstrip().split())
print(n//w)