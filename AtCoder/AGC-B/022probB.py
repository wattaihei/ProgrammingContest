N = int(input())

a, b = N//8, N%8

rep = [2, 3, 4, 6, 8, 9, 10, 12]

ans = []
for i in range(a):
    for r in rep:
        ans.append(12*i+r)

to = []
if b == 1:
    to = [6]
elif b == 2:
    to = [6, 12]
elif b == 3:
    to = [3, 6, 9]
elif b == 4:
    to = [2, 3, 4, 9]
elif b == 5:
    to = [2, 3, 4, 6, 9]
elif b == 6:
    to = [2, 3, 4, 8, 9, 10]
elif b == 7:
    to = [2, 3, 4, 6, 8, 9, 10]

for r in to:
    ans.append(12*a+r)

if N == 3:
    ans = [2, 5, 63]

for a in ans:
    print(a, end=' ')
print()