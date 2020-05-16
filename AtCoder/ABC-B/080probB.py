N = int(input())

A = sum([int(a) for a in list(str(N))])

if N % A == 0:
    print('Yes')
else:
    print('No')