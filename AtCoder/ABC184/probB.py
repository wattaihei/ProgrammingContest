import sys
input = sys.stdin.readline

N, X = map(int, input().rstrip().split())
S = list(input().rstrip())

for s in S:
    if s == "o":
        X += 1
    elif X > 0:
        X -= 1

print(X)