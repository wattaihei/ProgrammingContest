import sys
input = sys.stdin.buffer.readline

H, W, Q = map(int, input().rstrip().split())
dic = {}
ans = H*W
for _ in range(Q):
    y, x = map(int, input().rstrip().split())
    y -= 1; x -= 1
    d = dic.get(x, H)
    if d > y:
        ans -= (d-y)
        dic[x] = y
    print(ans)