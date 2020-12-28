import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))

P = []
must = [-1]*N
blank = 0
for i, (a, b) in enumerate(zip(A, B)):
    P.append(max(b-a+1, 0))
    if a <= b+1:
        must[i] = -1
    else:
        must[i] = a-(b+1)
