Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, b, n, S in Query:
    if a*n+b < S:
        ans = 'NO'
    else:
        rem = S - min(S//n, a)*n
        if rem > b:
            ans = 'NO'
        else:
            ans = 'YES'
    print(ans)