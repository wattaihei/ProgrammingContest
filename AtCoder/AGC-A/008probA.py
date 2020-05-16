x, y = map(int, input().split()) # 横に2個

if abs(x) <= abs(y):
    ans = abs(y) - abs(x)
    if (x >= 0 and y < 0) or (x < 0 and y > 0):
        ans += 1
    elif x < 0 and y < 0:
        ans += 2
else:
    ans = abs(x) - abs(y)
    if (x > 0 and y <= 0) or (x < 0 and y > 0):
        ans += 1
    elif (x > 0 and y > 0):
        ans += 2

print(ans)