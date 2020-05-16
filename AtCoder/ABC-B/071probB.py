S = input()

T = list('abcdefghijklmnopqrstuvwxyz')

for s in S:
    if s in T:
        T.remove(s)
if not T:
    print('None')
else:
    print(T[0])