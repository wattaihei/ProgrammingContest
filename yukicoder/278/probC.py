import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
print("Yes" if (a+b+c)%3 == 0 else "No")