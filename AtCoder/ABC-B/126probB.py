S = input()
x0 = int(S[:2])
x1 = int(S[2:])

if 0 < x0 <= 12 and 0 < x1 <= 12:
    print('AMBIGUOUS')
elif 0 < x0 <= 12:
    print('MMYY')
elif 0 < x1 <= 12:
    print('YYMM')
else:
    print('NA')