import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))

maxA = 0
ans = 0
for a, b in zip(A, B):
    maxA = max(a, maxA)
    ans = max(ans, maxA*b)
    print(ans)