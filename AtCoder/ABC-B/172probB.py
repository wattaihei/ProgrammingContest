import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

L = len(S)
ans = 0
for i in range(L):
    if S[i] != T[i]:
        ans += 1
print(ans)