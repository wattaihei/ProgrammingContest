# S[:i]の接頭辞と接尾辞が最大何文字一致しているか
def KMPTable(S):
    Table = [-1]
    j = -1
    for s in S:
        while j >= 0 and S[j] != s:
            j = Table[j]
        j += 1
        Table.append(j)
    return Table

# S[i:]とTが一致するiを求める
def KMPsearch(S, T):
    pass