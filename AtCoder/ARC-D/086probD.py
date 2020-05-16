N = int(input())
A = list(map(int, input().split()))

for l in range(N+1):
    B = A[:]
    ok = True
    ans = []
    if l < N:
        if A[l] <= 0:
            ok = False
        for r in range(l, N-1):
            a, b = B[r], B[r+1]
            if a == 0:
                if a <= b:
                    continue
                else:
                    ok = False
                    break
            if a <= b:
                count = 0
            else:
                count = (a-b)//a
                if b%a != 0: count += 1
            B[r+1] += a*count
            if count > 2:
                ok = False
                break
            ans += [(r+1, r+2)]*count
    
    while l > 0:
        if A[l-1] != 0:
            break
        l -= 1
    
    if l > 0:
        if A[l-1] >= 0:
            ok = False
        for r in range(l-1, 0, -1):
            a, b = B[r], B[r-1]
            if a == 0:
                if b <= a:
                    continue
                else:
                    ok = False
                    break
            if b <= a:
                count = 0
            else:
                count = (a-b)//a
                if b%a != 0: count += 1
            B[r-1] += a*count
            if count > 2:
                ok = False
                break
            ans += [(r+1, r)]*count
    if ok:
        print(len(ans))
        for a, b in ans:
            print(a, b)