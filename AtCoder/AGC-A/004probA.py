A, B, C = map(int, input().split()) # 横に2個

ans = A
for i in [A, B, C]:
    if i % 2 == 0:
        ans = 0

if ans != 0:
    F = []
    if C > 1:
        F.append(A*B)
    if B > 1:
        F.append(C*A)
    if A > 1:
        F.append(B*C)
    ans = min(F)

print(ans)