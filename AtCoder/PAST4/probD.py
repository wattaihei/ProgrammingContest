import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())

T = []
pre = "."
t = 0
for s in S:
    if s == ".":
        t += 1
    else:
        if t > 0:
            T.append(t)
        t = 0
    pre = s

if t > 0:
    T.append(t)

if not T:
    print(0, 0)
else:
    a1 = T[0] if S[0] == "." else 0
    a2 = T[-1] if S[-1] == "." else 0
    score = max(max(T), a1+a2)
    print(a1, score-a1)