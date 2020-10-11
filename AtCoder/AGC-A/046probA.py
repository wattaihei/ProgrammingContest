import sys
input = sys.stdin.readline

X = int(input())

a = 1
while a*X % 360 != 0:
    a += 1

print(a)