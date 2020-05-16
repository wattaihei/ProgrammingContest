N = int(input())
S = input()

ans = int(S)
for i in range(1, N):
    if S[i] == '0':
        continue
    a = S[:i]
    b = S[i:]
    
print(ans)