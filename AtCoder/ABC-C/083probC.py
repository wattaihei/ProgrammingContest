X, Y = map(int, input().split())

for i in range(300):
    if X * 2**i > Y:
        ans = i
        break
print(ans)