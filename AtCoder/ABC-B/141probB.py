S = list(input())

ans = 'Yes'
for i, s in enumerate(S):
    if i%2 == 0:
        if not s in ['R', 'U', 'D']:
            ans = 'No'
    if i%2== 1:
        if not s in ['L', 'U', 'D']:
            ans = 'No'
print(ans)