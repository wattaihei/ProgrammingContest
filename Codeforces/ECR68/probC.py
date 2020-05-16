
probs = []
Q = int(input())
for _ in range(Q):
    s = input()
    t = input()
    p = input()
    probs.append([s, t, p])

for prob in probs:
    s, t, p = prob

    ks = 0
    kt = 0
    want = []
    while ks < len(s) and kt < len(t):
        if s[ks] == t[kt]:
            ks += 1
            kt += 1
        else:
            want.append(t[kt])
            kt += 1
    ans = 'YES'

    if ks < len(s):
        ans = 'NO'
    else:
        want.extend(t[kt:])
        P = list(p)
        checked = [False for _ in range(len(P))]
        for w in want:
            OK = False
            for i, a in enumerate(P):
                if a == w and not checked[i]:
                    checked[i] = True
                    OK = True
                    break
            if not OK:
                ans = 'NO'
                break
    print(ans)
        


