N = int(input())

ans = 0
for n in range(1, N+1):
    if str(n).count("7") > 0: continue
    a = n
    ok = True
    while a > 0:
        if a%8 == 7:
            ok = False
            break
        a //= 8
    if ok:
        ans += 1
    
print(ans)