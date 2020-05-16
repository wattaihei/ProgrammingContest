S = input()

if (len(S)%2 == 0 and S[0] == S[-1]) or (len(S)%2 == 1 and S[0] != S[-1]):
    print('First')
else:
    print('Second')
