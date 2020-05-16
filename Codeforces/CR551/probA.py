N, T = map(int, input().split())
SD = [list(map(int, input().split())) for _ in range(N)]


wait = 10**9
for i, (s, d) in enumerate(SD):
    if s > T:
        w = s-T
    else:
        a = (T-s)//d*d
        if (T-s)%d != 0:
            a += d
        w =  a - (T-s)
    if w < wait:
        ind = i+1
        wait = w

print(ind)