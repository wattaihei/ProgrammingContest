A, B, C = map(int, input().split()) # 横に2個

co = 0
checked = []
if A % 2 != 0 or B % 2 != 0 or C % 2 != 0:
    print(0)
else:
    while True:
        checked.append([A, B, C])
        a = (B + C)//2
        b = (C + A)//2
        c = (A + B)//2
        co += 1
        if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
            break
        if [a, b, c] in checked:
            co = -1
            break
        A = a
        B = b
        C = c

    print(co)