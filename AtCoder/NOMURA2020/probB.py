import sys
input = sys.stdin.readline

S = input().rstrip()
T = ""
for s in S:
    if s == "?":
        T += "D"
    else:
        T += s
print(T)