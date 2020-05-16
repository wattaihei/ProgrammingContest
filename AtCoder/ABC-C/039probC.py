S = list(input())

A = []
for i in range(19):
    if S[i] == S[i+1]:
        A.append(i+1)
a = A[0]
if A[1] - A[0] == 7:
    # A[0]はミ
    if a == 1:
        print('Mi')
    if a == 3:
        print('Re')
    if a == 5:
        print('Do')
    if a == 6:
        print('Si')
    if a == 8:
        print('La')
    if a == 10:
        print('So')
    if a == 12:
        print('Fa')
else:
    # A[0] はシ
    if a == 1:
        print('Si')
    if a == 3:
        print('La')
    if a == 5:
        print('So')
    if a == 7:
        print('Fa')
    if a == 8:
        print('Mi')
    if a == 10:
        print('Re')
    if a == 12:
        print('Do')
