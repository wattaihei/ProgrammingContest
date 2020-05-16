x, y = map(int, input().split())

if y % 2 == 1:
    ans = -1
else:
    k = y//2
    if -k <= x <= k and (k-x)%2 == 0:
        ans = k
    else:
        ans = -1

print(ans)