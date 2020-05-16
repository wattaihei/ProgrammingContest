T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

d1 = T2*A2-T2*B2
d2 = T1*A1-T1*B1

if d1 + d2 == 0:
    print('infinity')
else:
    a = abs(d1//(d1+d2))
    ans = a*2-1
    print(ans)