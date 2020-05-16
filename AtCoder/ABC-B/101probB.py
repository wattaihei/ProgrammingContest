N = int(input())
S = sum([int(a) for a in list(str(N))])

if N % S == 0:
    print('Yes')
else:
    print('No')