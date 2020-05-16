import sys
input = sys.stdin.readline

lA, lB, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
XYZ = [list(map(int, input().split())) for _ in range(M)]

ans = min(A) + min(B)
dic = {}
for x, y, c in XYZ:
    ans = min(ans, A[x-1]+B[y-1]-c)

print(ans)