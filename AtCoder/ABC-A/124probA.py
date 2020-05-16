A, B = map(int, input().split()) # 横に2個

if A >= B + 1:
    print(A+(A-1))
elif B >= A + 1:
    print(B+(B-1))
else:
    print(A*2)