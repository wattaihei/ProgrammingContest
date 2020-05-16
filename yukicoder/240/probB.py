a, b, x, N = map(int, input().split())
if x%2 == 1:
    ans1 = 0
    ans2 = N//2
else:
    ans1 = N//2
    ans2 = 0

print(ans2, ans1)
