N = int(input())
A = list(map(int, input().split()))

ans = 'YES'
for i, a in enumerate(A):
    if i == 0:
        pre = a
        up = True
        continue
    if up and pre > a:
        up = False
    if not up and pre < a:
        ans = 'NO'
        break
    pre = a

print(ans)