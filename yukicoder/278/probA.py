import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

nums = [str(i) for i in range(10)]

ans = ""
for t in T:
    if t in nums:
        ans += S[int(t)]
    else:
        ans += t

print(ans)