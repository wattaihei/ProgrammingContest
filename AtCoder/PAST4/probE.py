from itertools import permutations

N = int(input())
S = list(input().rstrip())

ans = "None"
for T in permutations(S):
    E = list(T)
    if E != S and E[::-1] != S:
        ans = "".join(E)
        break

print(ans)
