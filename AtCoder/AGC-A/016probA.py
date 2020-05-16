S = input()
N = len(S)

dic = {}
for i, s in enumerate(S):
    if not s in dic.keys():
        dic[s] = [i]
    else:
        dic[s].append(i)

all = True
for i in range(N-1):
    if S[i] != S[i+1]:
        all = False


ans = N

for m in dic.keys():
    if all:
        ans = 0
        break
    q = list(S)
    c = 0
    allm = False
    while not allm:
        n = len(q)
        qq = []
        allm = True
        for i in range(n-1):
            if q[i] == m or q[i+1] == m:
                qq.append(m)
            else:
                allm = False
                qq.append(q[i])
        c += 1
        q = qq
    ans = min(ans, c)

print(ans)
