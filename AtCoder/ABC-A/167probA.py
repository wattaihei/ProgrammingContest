S = input()
T = input()
if len(S) == len(T) - 1 and T[:-1] == S:
    print("Yes")
else:
    print("No")