A, B = map(int, input().split())
S = list(input())

N = [str(a) for a in range(10)]
ans = 'Yes'
for i, s in enumerate(S):
    if i != A:
        if not s in N:
            ans = 'No'
    else:
        if s != '-':
            ans = 'No'
print(ans)