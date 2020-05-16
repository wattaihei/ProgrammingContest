import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
S = input().rstrip()
Query = []
for _ in range(Q):
    Alp, LR = map(str, input().rstrip().split())
    Query.append((Alp, LR))

S = "a" + S + "a"

left = 1
for Alp, LR in reversed(Query):
    if S[left-1] == Alp and LR == "R":
        left -= 1
    elif S[left] == Alp and LR == "L":
        left += 1

right = 1
for Alp, LR in reversed(Query):
    if S[-right] == Alp and LR == "L":
        right -= 1
    elif S[-1-right] == Alp and LR == "R":
        right += 1

print(max(0, N+2-left-right))