N = int(input())
A = [int(input()) for _ in range(N)]

Ls = []
for a in A:
    print(Ls)
    k = -1
    for i, l in enumerate(Ls):
        if l < a and a > k:
            ind = i
            k = a
    if k != -1:
        Ls[ind] = a
    else:
        Ls.append(a)


print(len(Ls))
