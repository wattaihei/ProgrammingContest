from collections import Counter

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    m = max(A)

    dic = {}
    for n in range((m+1)//2, m+1):
        dic[n] = 0

    for a in A:
        if not a in dic.keys():
            return False
        else:
            dic[a] += 1

    if m % 2 == 0:
        half = m//2
        if dic[half] != 1:
            return False
    else:
        half = m//2+1
        if dic[half] != 2:
            return False
    for n in range(half+1, m+1):
        if dic[n] < 2:
            return False
    return True


if __name__ == "__main__":
    if solve():
        print('Possible')
    else:
        print('Impossible')