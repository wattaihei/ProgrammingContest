A, B, C = map(int, input().split()) # 横に2個

K = A + B
if K < C:
    ans = A + B + 1 + B
elif K == C:
    ans = A + 2*B
else:
    ans = B + C
print(ans)