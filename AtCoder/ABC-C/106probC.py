S = input()
K = int(input())

c1 = 0
ans = S[0]
for i, s in enumerate(S):
    if s != '1':
        ans = s
        break
    c1 = i+1

if c1 >= K:
    print(1)
else:
    print(ans)