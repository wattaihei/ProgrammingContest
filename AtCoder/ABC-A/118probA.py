A, B = map(int, input().split()) # 横に2個

if B % A == 0:
    print(A + B)
else:
    print(B- A)