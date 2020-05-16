W, H, x, y = map(float, input().split()) # 横に2個


half = W * H / 2
print(half)

if 2*x == W and 2*y == H:
    print(1)
else:
    print(0)