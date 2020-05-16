import sys
input = sys.stdin.readline

S = list(input().rstrip())
L = len(S)

l = 0
r = L-1
ans = []
while l < r:
    while l < L and S[l] == ")":
        l += 1
    while r >= 0 and S[r] == "(":
        r -= 1
    if l < r:
        ans.append(l+1)
        ans.append(r+1)
        l += 1
        r -= 1

ans.sort()
if ans:
    print(1)
    print(len(ans))
    print(*ans)
else:
    print(0)