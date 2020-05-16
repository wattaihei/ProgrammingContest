N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

ans = A*N
for l in range(N+1):
    sto = H-l*E
    #print(l, sto, (N-l)*D+sto, (N-l)*B + sto)
    if (N-l)*D + sto > 0:
        price = (N-l)*C
    elif (N-l)*B + sto > 0:
        s = (N-l)*B + sto
        k = s//(B-D)
        if s%(B-D) == 0:
            k -= 1
        price = k*C + (N-l-k)*A
    else:
        continue
    #print(l, price)
    ans = min(ans, price)

print(ans)
