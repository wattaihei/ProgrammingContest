from collections import Counter

N, M = map(int, input().split())
S = list(input())
T = list(input())

Sc = Counter(S)
Tc = Counter(T)

ans = 0
for alp, num in Sc.items():
    if not alp in Tc.keys():
        ans = -1
        break
    a = num//Tc[alp]
    if num%Tc[alp] != 0: a += 1
    ans = max(ans, a)

print(ans)