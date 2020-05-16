S = input()
N = len(S)
ok = True
if N%2 == 0:
    for i in range(N//2):
        if S[2*i:2*i+2] != "hi":
            ok = False
else:
    ok = False
print("Yes" if ok else "No")