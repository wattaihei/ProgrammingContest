S = input()
T = input()
X = len(S)
Y = len(T)

com = False
for l in range(X-Y, -1, -1):
    for i in range(X-l):
        removed = S[:i] + S[i+l:]
        r = 0
        t = 0
        while t < X and r < len(removed):
            if T[t] == removed[r]:
                t += 1
                r += 1
            else:
                r += 1 
        if t == X:
            com = True
            ans = l
            break
    if com:
        break
print(ans)
            