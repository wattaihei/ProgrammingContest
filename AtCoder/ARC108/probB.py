import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())

T = []
for s in S:
    if s == "x" and len(T) > 1 and T[-1] == "o" and T[-2] == "f":
        T.pop()
        T.pop()
    else:
        T.append(s)

print(len(T))