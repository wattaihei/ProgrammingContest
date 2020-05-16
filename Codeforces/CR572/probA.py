N = int(input())
A = [int(a) for a in input()]

c0 = A.count(0)
c1 = A.count(1)

if c0 != c1:
    print(1)
    print(''.join([str(a) for a in A]))
else:
    for i in range(1, N):
        left = A[:i]
        right = A[i:]
        if left.count(0) != left.count(1) and right.count(0) != right.count(1):
            break
    print(2)
    print(''.join([str(l) for l in left]), ''.join([str(r) for r in right]))