N = int(input())
P = list(map(int, input().split()))

now_min = 10**9
ans = 0
for p in P:
    if p <= now_min:
        ans += 1
        now_min = p

print(ans)