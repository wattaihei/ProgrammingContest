A, B = map(int, input().split())

Aimax = (A-1)%50*2-1
Bimax = (B-1)%50*2-1
Ajmax = (A-1)//50
Bjmax = (B-1)//50

rowA1 = ['#' for _ in range(100)]
rowA2 = ['.' if i%2==0 else '#' for i in range(100)]
rowA3 = ['.' if i%2==0 and i <= Aimax else '#' for i in range(100)]

rowB1 = ['.' for _ in range(100)]
rowB2 = ['#' if i%2==0 else '.' for i in range(100)]
rowB3 = ['#' if i%2==0 and i <= Bimax else '.' for i in range(100)]

state = []

r = 0
for j in range(50):
    if j%2 == 0 and r < Ajmax:
        state.append(rowA2)
        r += 1
    elif j%2 == 0 and r == Ajmax:
        state.append(rowA3)
        r += 1
    else:
        state.append(rowA1)

r = 0
for j in range(50):
    if j%2 == 1 and r < Bjmax:
        state.append(rowB2)
        r += 1
    elif j%2 == 1 and r == Bjmax:
        state.append(rowB3)
        r += 1
    else:
        state.append(rowB1)

print(100, 100)
for s in state:
    print(''.join(s))