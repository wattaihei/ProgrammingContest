N = int(input())
W = list(map(int, input().split()))

for T in range(1, N):
    little = 0
    for Wl in W[:T]:
        little += Wl
    large = 0
    for Wg in W[T:]:
        large += Wg
    Abs_now = abs(large - little)
    if T == 1:
        Abs = Abs_now
    if Abs_now < Abs:
        Abs = Abs_now

print(Abs)
