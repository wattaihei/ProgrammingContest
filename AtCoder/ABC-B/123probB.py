A = [int(input()) for _ in range(5)]

time = 0
amari = 10
for a in A:
    am = a % 10
    if am == 0:
        time += (a // 10) * 10
    else:
        time += (a // 10 + 1) * 10
        if am < amari:
            amari = am
k = 0 if amari == 10 else 10 - amari
time -= k
print(time)