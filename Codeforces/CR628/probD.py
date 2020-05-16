import sys
input = sys.stdin.readline

u, v = map(int, input().split())

if u == v == 0:
    print(0)
elif u == v:
    print(1)
    print(u)
elif v > u and (v-u)%2 == 0:
    a = (v-u)//2
    if u&a:
        print(3)
        print(a, a, u)
    else:
        print(2)
        x = a|u
        print(x, a)
else:
    print(-1)