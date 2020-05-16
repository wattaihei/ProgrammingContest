A = list(map(int, input().split()))

ans = A[1]
B = [A[0], A[3], A[4]]
C = []
for b in B:
    if b == 0:
        C.append(0)
        continue
    a = (b-1)//2
    ans += a*2
    C.append(b-a*2)

if C.count(2) >= 2:
    for c in C:
        ans += c//2*2
elif min(C) == 1:
    ans += 3
else:
    for c in C:
        ans += c//2*2

print(ans)