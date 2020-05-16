N = int(input())
S = input()

n = 0
for s in S:
    if s == '-':
        if n > 0:
            n -= 1
    elif s == "+":
        n += 1
print(n)