T = list(input())
L = len(T)

c = 0
ans = 0
five = False
two = False
w = 0
for i in range(L):
    t = T[i]
    if t == '2':
        if w == 0 and not five:
            c = 0
        elif w%2 == 0:
            if five:
                c += w
            else:
                ans = max(ans, (c+w)//2*2)
                c = w  
        else:
            if two:
                c += w
            else:
                ans = max(ans, (c+w)//2*2)
                c = w//2*2
        c += 1
        two = True
        five = False
        w = 0
    elif t == '5':
        if w == 0 and not two:
            c = 0
        elif w%2 == 0:
            if two:
                c += w
            else:
                ans = max(ans, (c+w)//2*2)
                c = w
        else:
            if five:
                c += w
            else:
                ans = max(ans, (c+w)//2*2)
                c = w
        if c > 0:
            c += 1
        w = 0
        five = True
        two = False
    elif t == '?':
        w += 1
    else:
        w = 0
        c = 0
        five = False
        two = False
    #print(t, c, w, two, five)
    ans = max(ans, c//2*2)
ans = max(ans, (c+w)//2*2)
print(ans)