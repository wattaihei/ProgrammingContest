N = int(input())

def mod(mod, n):
    i = 0
    if n < mod:
        return 0, n
    while n >= mod**i:
        a, b = i, n-mod**i
        i += 1
    return a, b

checked6 = [False for _ in range(N)]
checked9 = [False for _ in range(N)]
def draw(remain, c):
    checked[remain-1] = True
    print('roop', remain)
    c6, re6 = mod(6, remain)
    c9, re9 = mod(9, remain)
    print(c6, re6)
    print(c9, re9)
    if c6 == 0:
        c += re6
        return c
    if c9 == 0:
        c += re9
        return c
    c_6 = c + draw(re6, c) + 1
    c_9 = c + draw(re9, c) + 1
    return min(c_6, c_9)

print(draw(N, 0))