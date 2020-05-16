N, X = map(int, input().split())
S = input()
T = [int(input()) for _ in range(N)]

ans = 0
for i, t in enumerate(T):
    if S[i] == "1":
        ans += min(t, X)
    else:
        ans += t
print(ans)