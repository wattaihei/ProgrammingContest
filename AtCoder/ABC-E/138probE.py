from bisect import bisect_left, bisect_right


def main():
    S = list(input())
    T = list(input())
    sl = len(S)

    Sdic = {}
    for i, s in enumerate(S):
        if not s in Sdic.keys():
            Sdic[s] = [i]
        else:
            Sdic[s].append(i)
    pret = -1
    ans = 0
    for t in T:
        try:
            #print(Sdic[t])
            it = bisect_right(Sdic[t], pret)
            #print(it, t)
            if it < len(Sdic[t]):
                pret = Sdic[t][it]
            else:
                ans += sl
                pret = Sdic[t][0]
            #print(t, update, pret)
        except KeyError:
            ans = -1
            break
    if ans != -1:
        ans += pret+1
    print(ans)

if __name__ == "__main__":
    main()