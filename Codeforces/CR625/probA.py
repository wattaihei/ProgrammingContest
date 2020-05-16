import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

p = 0
q = 0
for a, b in zip(A, B):
    if a == 1 and b == 0:
        p += 1
    elif a == 0 and b == 1:
        q += 1

if p == 0:
    print(-1)
else:
    print((q+p)//p)