Q = int(input())

Qs = []
for _ in range(Q):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    Qs.append([b, p, f, h, c])

for b, p, f, h, c in Qs:
    if 2*(p + f) <= b:
        ans = h*p + f*c
    elif h > c:
        if 2*p <= b:
            ans = h*p + c*((b-2*p)//2)
        else:
            ans = h*(b//2)
    else:
        if 2*f <= b:
            ans = c*f + h*((b-2*f)//2)
        else:
            ans = c*(b//2)
    print(ans)