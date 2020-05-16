N = int(input())
A = list(map(int, input().split()))

a4 = 0
a2 = 0
a0 = 0
for a in A:
    if a % 4 == 0:
        a4 += 1
    elif a % 4 == 2:
        a2 += 1
    else:
        a0 += 1

if a2 == 0:
    if a4 >= a0-1:
        print('Yes')
    else:
        print('No')
elif a0 == 0:
    print('Yes')
else:
    if a4 >= a0:
        print('Yes')
    else:
        print('No')