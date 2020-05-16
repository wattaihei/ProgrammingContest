K = int(input())
B = list(map(int, input().split()))

A = B[::-1]

l = 2
m = 2
ok = True
prea = 2
for a in A:
    nl = (l + prea - 1)//a * a

    if m%a == 0:
        m -= 1
    nm = (m//a + 1) * a
    #print(a, m, nl, l, prea)
    if nm == 0 or nl < l or nl >= l + prea:
        ok = False
        break
    prea = a
    l = nl
    m = nm
if A[0] != 2:
    ok = False

if not ok:
    print(-1)
else:
    print(m, l+prea-1)