S = list(map(int, input().split('/')))

if S[0] > 2019:
    ans = 'TBD'
elif S[0] < 2019:
    ans = 'Heisei'
else:
    if S[1] > 4:
        ans = 'TBD'
    elif S[1] <= 4:
        ans = 'Heisei'

print(ans)