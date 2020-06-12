import sys
input = sys.stdin.readline

S = input().rstrip()

L = len(S)
ans = 0
for i in range(L-1):
    if S[i+1] != "0":
        ans += 1
print(ans)