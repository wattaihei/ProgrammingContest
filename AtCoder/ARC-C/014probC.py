N = int(input())
S = input()

ans = 0
for s in ['R', 'G', 'B']:
    ans += S.count(s) % 2
print(ans)