N = int(input())

if N%2 == 0:
    print('NO')
else:
    print('YES')
    ans = [None]*(2*N)
    for k in range(1, N+1):
        if k%2 == 1:
            ans[k-1] = 2*k-1
            ans[N+k-1] = 2*k
        else:
            ans[k-1] = 2*k
            ans[N+k-1] = 2*k-1
    for a in ans:
        print(a, end=' ')
    print()