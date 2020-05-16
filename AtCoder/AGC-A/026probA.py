N = int(input())
A = list(map(int, input().split()))

ans = 0
pre = -1
cont = 1
for a in A:
    if a == pre:
        cont += 1
    else:
        ans += cont // 2
        cont = 1
    pre = a
if cont != 1:
    ans += cont // 2
print(ans)