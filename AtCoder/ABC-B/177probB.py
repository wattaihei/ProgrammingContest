S = input()
T = input()

ls = len(S)
lt = len(T)

ans = ls
for i in range(ls-lt+1):
    c = 0
    for j in range(lt):
        if S[i+j] != T[j]:
            c += 1
    ans = min(ans, c)
print(ans)