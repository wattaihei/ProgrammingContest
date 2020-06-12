import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for H, W in Query:
    if H%2 == 0:
        ans = H//2 * W
    elif W % 2 == 0:
        ans = W//2 * H
    else:
        ans = W*H//2+1
    print(ans)