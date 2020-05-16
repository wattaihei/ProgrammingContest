H = int(input())
W = int(input())
N = int(input())

m = max(H, W)
ans = N//m
if N%m != 0:
    ans += 1
print(ans)