import sys
input = sys.stdin.readline

H, W = map(int, input().split())
if H == 1 or W == 1:
    ans = 1
elif H%2 == 1 and W%2 == 1:
    ans = H*(W//2) + (H+1)//2
else:
    ans = H*W//2
print(ans)