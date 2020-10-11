S = input()
N = len(S)

ans  = -1
for i in range(1, N):
    T = S[:i]
    if len(T)%2 != 0: continue
    if T[:i//2] == T[i//2:]:
        ans = i
print(ans)