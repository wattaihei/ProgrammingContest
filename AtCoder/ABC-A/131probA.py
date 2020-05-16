S = [int(i) for i in list(input())]

D = False
for i, num in enumerate(S):
    if i == 0:
        pre = num
    else:
        if num == pre:
            D = True
        pre = num

if D:
    print('Bad')
else:
    print('Good')