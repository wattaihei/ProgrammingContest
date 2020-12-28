import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c, d = map(int, input().rstrip().split())
print(a*d - b*c)