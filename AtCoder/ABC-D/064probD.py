N = int(input())
S = input()

l = 0
r = 0
for i in range(N):
    if S[i] == '(':
        r += 1
    else:
        if r > 0:
            r -= 1
        else:
            l += 1
ans = '('*l + S + ')'*r
print(ans)