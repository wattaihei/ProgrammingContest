S = input()

L = len(S)
T = S[::L//2]
U = S[L//2+1:]

if S[::-1] == S and T[::-1] == T and U[::-1] == U:
    print("Yes")
else:
    print("No")