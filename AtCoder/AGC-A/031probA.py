N = int(input())
S = input()

num = {}
for s in S:
    if s in num.keys():
        num[s] += 1
    else:
        num[s] = 1

ans = 1
for n in num.values():
    ans = int(ans * (n+1) % (1E9+7))

ans -= 1

print(ans)