N = int(input())
S = list(input())
T = list(input())

ab = []
ba = []
for i in range(N):
    if S[i] == 'a' and T[i] == 'b':
        ab.append(i)
    elif S[i] == 'b' and T[i] == 'a':
        ba.append(i)

if (len(ab)+len(ba)) % 2 == 1:
    print(-1)
else:
    c = (len(ab)+len(ba)) // 2
    change = -1
    if len(ab) % 2 == 1:
        k = ab.pop()
        ba.append(k)
        change = k
        c += 1
    print(c)
    if change != -1:
        print(change+1, change+1)
    for i in range(len(ab)//2):
        print(ab[2*i]+1, ab[2*i+1]+1)
    for i in range(len(ba)//2):
        print(ba[2*i]+1, ba[2*i+1]+1)