N, A, B, C, D = map(int, input().split()) # 横に2個
S = [0 if s == '.' else 1  for s in input()]

if C <= B:
    ans = 'Yes'
    for i in range(A, C):
        if S[i] == 1 and S[i-1] == 1:
            ans = 'No'
            break
    for i in range(B, D):
        if S[i] == 1 and S[i-1] == 1:
            ans = 'No'
            break

elif C < D:
    ans = 'Yes'
    for i in range(A, D):
        if S[i] == 1 and S[i-1] == 1:
            ans = 'No'
            break
else:
    ans = '?'
    for i in range(A, C):
        if S[i] == 1 and S[i-1] == 1:
            ans = 'No'
            break
        if B - 1 <= i <= D - 1 and S[i] == 0 and S[i-1] == 0 and S[i+1] == 0:
            ans = 'Yes'
            break
    if ans == '?':
        ans = 'No'

print(ans)
