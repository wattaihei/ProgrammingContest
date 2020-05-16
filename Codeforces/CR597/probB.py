Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A, B, C = map(int, input().split())
    S = input()
    Query.append((N, A, B, C, S))

for N, A, B, C, S in Query:
    dic = {'R': A, 'P':B, 'S':C}
    ans = []
    for i in range(N):
        if S[i] == 'R':
            if dic['P'] > 0:
                dic['P'] -= 1
                ans.append('P')
            else:
                ans.append('W')
        elif S[i] == 'P':
            if dic['S'] > 0:
                dic['S'] -= 1
                ans.append('S')
            else:
                ans.append('W')
        else:
            if dic['R'] > 0:
                dic['R'] -= 1
                ans.append('R')
            else:
                ans.append('W')
    if ans.count('W') > N//2:
        print('NO')
    else:
        print('YES')
        for i in range(N):
            if ans[i] == 'W':
                if dic['P'] > 0:
                    dic['P'] -= 1
                    ans[i] = 'P'
                elif dic['R'] > 0:
                    dic['R'] -= 1
                    ans[i] = 'R'
                else:
                    dic['S'] -= 1
                    ans[i] = 'S'
        print(''.join(ans))