S = input()
T = input()

if S == T:
    print("same")
else:
    ok = True
    for s, t in zip(list(S), list(T)):
        if not ord(s) - ord(t) in [0, 32, -32]:
            ok = False
    if ok:
        print("case-insensitive")
    else:
        print("different")