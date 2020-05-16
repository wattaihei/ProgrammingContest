S = input()

L = len(S)

for l in range(L//2-1, -1, -1):
    if S[:l] == S[l:2*l]:
        print(2*l)
        break