from collections import Counter

N = int(input())
S = input()
Q = int(input())
Query = [input() for _ in range(Q)]

dic = {}
for i, s in enumerate(S):
    if not s in dic.keys():
        dic[s] = [i]
    else:
        dic[s].append(i)

for T in Query:
    ans = 0
    C = Counter(list(T))
    for alp, num in C.items():
        ans = max(dic[alp][num-1]+1, ans)
    print(ans)