S = input()
N = len(S)

def dream(k):
    if k == N:
        return True
    if S[k] == 'd':
        if k+7 <= N:
            if S[k:k+7] == 'dreamer':
                if dream(k+7):
                   return True
        if k+5 <= N:
            if S[k:k+5] == 'dream':
                if dream(k+5):
                    return True
    elif S[k] == 'e':
        if k+6 <= N:
            if S[k:k+6] == 'eraser':
                if dream(k+6):
                    return True
        if k+5 <= N:
            if S[k:k+5] == 'erase':
                if dream(k+5):
                    return True
    return False

a = dream(0)
if a:
    print('YES')
else:
    print('NO')