S = list(input())

a = 0
for i, s in enumerate(S):
    if i%2==0:
        if s == "p":
            a -= 1
    if i%2==1:
        if s == "g":
            a += 1
print(a)