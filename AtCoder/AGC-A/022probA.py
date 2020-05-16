import string

S = input()

abc = [chr(i) for i in range(97, 97+26)]

if len(S) < 26:
    for s in S:
        abc.remove(s)
    add = abc[0]
    print(S + add)
elif S == ''.join(sorted(abc, reverse=True)):
    print(-1)
else:
    N = len(S)
    for i in range(1, N):
        now = S[N-i-1]
        fow = S[N-i:]
        fows = sorted(list(fow))
        for f in fows:
            if now < f:
                now = f
                break
        if now != S[N-i-1]:
            ans = S[:N-i-1] + now
            break
    print(ans)

