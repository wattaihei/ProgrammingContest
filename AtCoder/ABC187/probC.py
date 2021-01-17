import sys
input = sys.stdin.readline

N = int(input())

noe = set()
withe = set()
for _ in range(N):
    S = input().rstrip()
    if S[0] == "!":
        withe.add(S[1:])
    else:
        noe.add(S)

ans = "satisfiable"
for S in withe:
    if S in noe:
        ans = S
        break
print(ans)