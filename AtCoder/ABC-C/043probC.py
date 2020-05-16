N = int(input())
A = list(map(int, input().split()))

ans = 200**2*1000
for k in range(-100, 101):
    l = 0
    for a in A:
        l += abs(a-k)**2
    ans = min(ans, l)

print(ans)