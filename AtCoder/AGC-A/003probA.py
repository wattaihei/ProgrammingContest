S = input()

no = False
so = False
ea = False
we = False
for s in S:
    if s == 'N':
        no = True
    elif s == 'S':
        so = True
    elif s == 'E':
        ea = True
    elif s == 'W':
        we = True

if ((no and so) or (not no and not so)) and ((ea and we) or (not ea and not we)):
    print('Yes')
else:
    print('No')