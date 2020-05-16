D, G = map(int, input().split())
PC = [list(map(int, input().split())) for _ in range(D)]

def com(d, s, ans):
    if d == D:
        ans.append(s)
        return ans
    a = s[:]
    a.append(1)
    ans = com(d+1, a, ans)
    b = s[:]
    b.append(0)
    ans = com(d+1, b, ans)
    return ans

L = com(0, [], [])
ans = 10000
for l in L:
    point = 0
    probs = 0
    uncom = []
    for i, com in enumerate(l):
        if com == 0:
            uncom.append(i)
        else:
            p, c = PC[i]
            point += (i+1)*100*p + c
            probs += p
    #print(probs, l)
    if point >= G:
        ans = min(ans, probs)
        continue
    uncom.sort(reverse=True)
    re = G - point
    for un in uncom:
        p, c = PC[un]
        #print(re, probs, p)
        if (un+1)*100*(p-1) >= re:
            rem = 1 if re % ((un+1)*100) > 0 else 0
            probs += re // ((un+1)*100) + rem
            re = 0
            break
        re -= (un+1)*100*(p-1)
        probs += p-1
    #print(probs)
    if re > 0:
        continue
    ans = min(ans, probs)
print(ans)