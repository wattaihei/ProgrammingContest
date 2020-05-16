

def ask(c1, c2):
    print('?', c1, c2)
    ans = input()
    if ans == '<':
        return [c1, c2]
    if ans == '>':
        return [c2, c1]


def match(left_sorted, right_sorted, matched_list):
    if len(left_sorted) == 0:
        return matched_list + right_sorted
    if len(right_sorted) == 0:
        return matched_list + left_sorted
    l0 = left_sorted[0]
    r0 = right_sorted[0]
    if ask(l0, r0)[0] == l0:
        matched_list.append(l0)
        nleft_sorted = left_sorted[1:]
        for_return = match(nleft_sorted, right_sorted, matched_list)
    else:
        matched_list.append(r0)
        nright_sorted = right_sorted[1:]
        for_return = match(left_sorted, nright_sorted, matched_list)
    return for_return



def sort(sort_list):
    if len(sort_list) == 1:
        return sort_list
    elif len(sort_list) == 2:
        c1 = sort_list[0]
        c2 = sort_list[1]
        return ask(c1, c2)
    else:
        mid = len(sort_list) // 2
        left_list = sort_list[:mid]
        right_list = sort_list[mid:]
        left_sorted = sort(left_list)
        right_sorted = sort(right_list)
        init_list = []
        matched_list = match(left_sorted, right_sorted, init_list)
        return matched_list


def main():
    N, Q = map(int, input().split())
    alp_list = [chr(i) for i in range(65, 65+N)]
    alp_sorted = sort(alp_list)
    print('!', ''.join(alp_sorted))


if __name__=='__main__':
    main()