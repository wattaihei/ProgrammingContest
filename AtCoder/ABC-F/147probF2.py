import sys
input = sys.stdin.readline

N, X, D = map(int, input().split())

if D == 0:
    ans = N+1 if X != 0 else 1
else:
    C = {}
    Que = {}
    for l in range(N+1):
        start = l*X//D + l*(l-1)//2
        end = start + l*(N-l)
        key = l*X%D
        if key in Que:
            Que[key].append((start, end))
            C[key] += [start, end, start+1, end+1, start-1, end-1]
        else:
            Que[key] = [(start, end)]
            C[key] = [start, end, start+1, end+1, start-1, end-1]


    ans = 0
    for key, List in C.items():
        ind_to_co = sorted(list(set(List)))
        co_to_ind = {a:i for i, a in enumerate(ind_to_co)}

        Imos = [0]*(len(ind_to_co)+1)
        for start, end in Que[key]:
            Imos[co_to_ind[start]] += 1
            Imos[co_to_ind[end+1]] -= 1

        for i in range(len(ind_to_co)-1):
            a = ind_to_co[i]; b = ind_to_co[i+1]
            Imos[i+1] += Imos[i]
            if Imos[i+1] > 0 and Imos[i] > 0:
                ans += b-a
            elif Imos[i] > 0:
                ans += 1
print(ans)