S = input()
L = len(S)
k = 0
for i in range(L):
    if S[i] != S[-i-1]:
        k += 1
print(k//2)