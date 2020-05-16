N, x = map(int, input().split()) # 横に2個
A = list(map(int, input().split()))


ans = 0
curll = []
for i, a in enumerate(A):
    k = a
    ind = i
    curl = False
    count = 0
    cost = a
    minc = 0
    while k > 0 or count < N:
        count += 1
        if ind == N-1:
            ind = 0
        else:
            ind += 1
        if k > A[ind] + x:
            cost0 = A[ind] + x*count
            if cost0 < cost:
                cost = cost0
                minc = count
            curl = True
        k -= x
    if not curl:
        ans += a
    else:
        ans += cost - x*minc
        curll.append(minc)

if curll:
    ans += max(curll)*x

print(ans)