X = int(input())
N = X

a = 0
while N > 1:
    #print(N)
    if a % 2 == 0 and N != 2:
        N = N // 2 + 1
    else:
        N = N // 2 
    a += 1

if a % 2 == 1 or X == 1:
    print('Aoki')
else:
    print('Takahashi')