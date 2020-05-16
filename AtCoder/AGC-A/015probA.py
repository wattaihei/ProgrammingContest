N, A, B = map(int, input().split()) # 横に2個

if A < B and N > 1:
    ans = (B*(N-1)+A) -  (A*(N-1)+B) + 1
elif A < B and N == 1:
    ans = 0
elif A > B:
    ans = 0
else:
    ans = 1

print(ans)