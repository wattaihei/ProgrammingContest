N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

c = 0
sum = 0
for b in a:
    if sum + b <= x:
        c += 1
        sum += b
    else:
        break
if c == N and sum != x:
    c -= 1
print(c)