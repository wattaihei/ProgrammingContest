N, X = map(int, input().split()) # 横に2個

X = X if 2*X <= N else N - X
a = X
b = (N-X)//X
c = (N-X)%X
ans = 0
while True:
    ans += a*b*3
    if c == 0:
        break
    a, b, c = c, a//c, a%c

print(ans)