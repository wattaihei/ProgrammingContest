X, Y = map(int, input().split())

ok = False
for i in range(100):
    for j in range(100):
        if i+j == X and 4*i+2*j == Y:
            ok = True
            break
print("Yes" if ok else "No")