N, M = map(int, input().split())
P = [int(input()) for _ in range(N-1)]
q = [list(map(int, input().split())) for _ in range(M)]

Q = [0]*N
for p in P:
    Q[p] += 1

ans = 0
while q:
    dic = {}
    dic2 = {}
    for b, c in q:
        a = P[b-1]
        if not a in dic.keys():
            dic[a] = [c]
            dic2[a] = [(b, c)]
        else:
            dic[a].append(c)
            dic2[a].append((b, c))
    qq = []
    for k, v_list in dic.items():
        #print(k, v_list, Q[k])
        if len(v_list) != Q[k]:
            for v in dic2[k]:
                qq.append(v)
            continue
        if k == 0:
            ans += sum(v_list)
            continue
        ans += sum(v_list) - min(v_list)*len(v_list)
        qq.append([k, min(v_list)])
    #print(qq, ans)
    q = qq
print(ans)