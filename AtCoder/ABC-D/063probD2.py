N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]

l = 0
r = max(H)
T = 1
while r > l+1:
    T = (l+r)//2
    c = 0
    for h in H:
        if h > B*T:
            c += (h-B*T)//(A-B)
            if (h-B*T)%(A-B) != 0:
                c += 1
    if c <= T:
        r = T
    else:
        l = T

if l == T:
    print(T+1)
else:
    print(T)