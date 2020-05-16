N = int(input())
P = list(map(int, input().split()))

a = 0
for i, p in enumerate(P):
    if i+1 != p:
        a += 1

if a == 0 or a == 2:
    print('YES')
else:
    print('NO')
