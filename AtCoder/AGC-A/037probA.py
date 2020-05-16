S = list(input())

pre = ''
ans = 0
two = False
for s in S:
    if pre == s:
        two = True
        pre = ''
        continue
    pre = s
    if two:
        pre = ''
        two = False
    ans += 1
print(ans)