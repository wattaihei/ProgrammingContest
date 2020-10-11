N = int(input())
S = input()

T = ""
for s in S:
    a = ord(s) + N
    if a > ord("Z"):
        a -= 26
    T += chr(a)

print(T)