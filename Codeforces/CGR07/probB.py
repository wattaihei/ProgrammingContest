import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))

X = [0]
A = [B[0]]

for i, b in enumerate(B):
    if i == 0: continue
    X.append(max(X[-1], A[-1]))
    A.append(b+X[-1])

print(*A)