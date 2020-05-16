
N = int(input())
S = input()
ok = True
if N%2 == 1:
    ok = False
else:
    for i in range(N//2):
        if S[i] != S[i+N//2]:
            ok = False
if ok:
    print('Yes')
else:
    print('No')