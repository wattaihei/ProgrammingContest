import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

s = A[0]
for i in range(1, N):
    a = A[i]
    if a == s:
        print("stay")
    elif a > s:
        print("up", a-s)
    else:
        print("down", s-a)
    s = a