a = [int(input()) for _ in range(5)]
k = int(input())

if a[-1] - a[0] > k:
    print(':(')
else:
    print('Yay!')