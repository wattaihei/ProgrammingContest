A, B = map(int, input().split())

if A >= B:
    L, M = A, B
    a = '#'
    b = '.'
elif A < B:
    L, M = B, A
    a = '.'
    b = '#'

row1 = [a if j % 2 == 1 else b for j in range(100)]
row2 = [a if j % 2 == 0 else b for j in range(100)]
rowb = [a for _ in range(100)]

limax = L%50
if limax == 0:
    limax = 50

mimax = M%50
if mimax == 0:
    mimax = 50

mid1 = [b if i == 0 else a for i in range(100)]
mid2 = [a if i == 99 else b for i in range(100)]
mid3 = [b if i%2==0 and i <= limax*2-1 else a for i in range(100)]
mid4 = [a if i%2==1 and (100-i) <= mimax*2 else b for i in range(100)]

lmax = L//50
if L % 50 == 0:
    lmax -= 1

mmax = M//50
if M %50 == 0:
    mmax -= 1

state = []
c = 0
mid = False
while c < lmax:
    if c < mmax:
        state.append(row1)
        state.append(row2)
        c += 2
    elif not mid:
        state.append(rowb)
        state.append(mid3)
        state.append(mid1)
        state.append(mid2)
        state.append(mid4)
        state.append(mid2)
        state.append(rowb)
        mid = True
        continue
    else:
        state.append(rowb)
        state.append(row1)
        c += 1

if not mid:
    if mimax != 0:
        state.append(rowb)
        state.append(mid3)
        state.append(mid1)
        state.append(mid2)
        state.append(mid4)
        state.append(mid2)
        state.append(rowb) 
    else:
        state.append(rowb)

print(len(state), 100)
for s in state:
    print(''.join(s))