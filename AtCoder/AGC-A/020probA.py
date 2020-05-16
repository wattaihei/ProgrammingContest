N, A, B = map(int, input().split()) # 横に2個

if A == N-1 and B == N:
    print('Borys')
elif (B-A) % 2 == 0:
    print('Alice')
else:
    print('Borys')