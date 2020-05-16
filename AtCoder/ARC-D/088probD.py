S = input()
N = len(S)

if N%2 == 1:
    ans = N//2
    s = S[N//2]
    a = N//2+1
    for i in range(N//2+1):
        if S[N//2+i] != s or S[N//2-i] != s:
            a = i
            break
    ans += a
else:
    ans = N//2
    s = S[N//2]
    a = N//2
    for i in range(N//2):
        if s != S[N//2-1-i] or s != S[N//2+i]:
            a = i
            break
    ans += a
print(ans)