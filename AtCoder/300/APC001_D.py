import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
limit = sum(B) - sum(A)

if limit < 0:
    print("No")
else:
    need = 0
    for a, b in zip(A, B):
        if b < a:
            need += a-b
    can = 0
    for a, b in zip(A, B):
        if a < b:
            can += (b-a)//2
    if need > can:
        print("No")
    else:
        print("Yes")