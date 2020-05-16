A = list(map(int, input().split()))
A.sort()

if A[1] == 1:
    print(1000000)
else:
    ans = 0
    for a in A:
        if a == 1:
            ans += 300000
        elif a == 2:
            ans += 200000
        elif a == 3:
            ans += 100000
    print(ans)