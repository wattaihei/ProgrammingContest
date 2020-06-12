S1, S2 = input().split()

def calc(S):
    if S[0] == "B":
        return -int(S[1])+1
    return int(S[0])

print(abs(calc(S1)-calc(S2)))