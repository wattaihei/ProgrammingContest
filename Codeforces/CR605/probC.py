import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(input().rstrip())
Alp = set(list(input().rstrip().split()))
S.append("1")
last = -1
ans = 0
for i, s in enumerate(S):
    if not s in Alp:
        d = i-last-1
        ans += d*(d+1)//2
        last = i

print(ans)