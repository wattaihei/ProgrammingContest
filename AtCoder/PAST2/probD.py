S = input()

Alp = [chr(i) for i in range(97, 97+26)] + ["."]

def check(S1, S2):
    for s1, s2 in zip(S1, S2):
        if s1 != s2 and s1 != ".":
            return False
    return True

# 1
ans = len(set(list(S))) + 1

# 2
for a in Alp:
    for b in Alp:
        s = a + b
        for i in range(len(S)-1):
            if check(s, S[i:i+2]):
                ans += 1
                break

# 3
for a in Alp:
    for b in Alp:
        for c in Alp:
            s = a + b + c
            for i in range(len(S)-2):
                if check(s, S[i:i+3]):
                    ans += 1
                    break

print(ans)