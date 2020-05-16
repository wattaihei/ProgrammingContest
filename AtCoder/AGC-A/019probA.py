Q, H, S, D = map(int, input().split()) # 横に2個
N = int(input())

com = [Q*8, H*4, S*2, D]
com.sort()
price = (N // 2) * com[0]

if N % 2 == 1:
    am = [Q*4, H*2, S]
    am.sort()
    price += am[0]

print(price)