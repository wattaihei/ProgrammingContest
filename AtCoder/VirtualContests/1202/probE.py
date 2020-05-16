A, B = map(int, input().split())

whiteline = list("."*100)
blackline = list("#"*100)
checkline = ["." if i%2 == 0 else "#" for i in range(100)]

ans = []
b = B-1
for h in range(21):
    if h%2 == 0:
        ans.append(whiteline)
    else:
        if b >= 50:
            ans.append(checkline)
            b -= 50
        elif b > 0:
            P = list("."*100)
            for i in range(b):
                P[2*i] = "#"
            b = 0
            ans.append(P)
        else:
            ans.append(whiteline)
a = A-1
for h in range(21):
    if h%2 == 0:
        ans.append(blackline)
    else:
        if a >= 50:
            ans.append(checkline)
            a -= 50
        elif a > 0:
            P = list("#"*100)
            for i in range(a):
                P[2*i] = "."
            a = 0
            ans.append(P)
        else:
            ans.append(blackline)

print(len(ans), len(ans[0]))
for L in ans:
    print("".join(L))