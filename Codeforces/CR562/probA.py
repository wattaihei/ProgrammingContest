N, A, X, B, Y = map(int, input().split())

ok = False

while True:

    if A + 1 > N:
        A = 1
    else:
        A += 1
    if B > 1:
        B -= 1
    else:
        B = N
    
    if A == B:
        ok = True
        break
    
    if A == X or B == Y:
        break

if ok:
    print('YES')
else:
    print('NO')