A, B = map(int, input().split())

k = B%4
if A%2 == 0:
    if k == 0 or k == 3:
        print('Devil')
    else:
        print('Angel')
else:
    if k == 0:
        print('Devil')
    else:
        print('Angel')