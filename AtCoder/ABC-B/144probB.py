N = int(input())

ok = False
for n in range(1, 10):
    if N%n == 0 and N//n < 10:
        ok = True

if ok:
    print('Yes')
else:
    print('No')