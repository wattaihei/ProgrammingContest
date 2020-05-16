
def main():
    N = int(input())

    checked = [0]*(N+1)

    print(0)
    A = input()
    if A == 'Vacant':
        return
    elif A == 'Male':
        checked[0] = 1
        checked[N] = 1
    else:
        checked[0] = -1
        checked[N] = -1
    l = 0
    r = N
    m = (l+r)//2
    while l < r:
        print(m)
        A = input()
        if A == 'Vacant':
            return
        elif A == 'Male':
            checked[m] = 1
        else:
            checked[m] = -1

        if (m - l) % 2 == 1:
            if checked[l] != checked[m]:
                l = m
            else:
                r = m
        else:
            if checked[l] == checked[m]:
                l = m
            else:
                r = m
        m = (l+r)//2



if __name__ == "__main__":
    main()