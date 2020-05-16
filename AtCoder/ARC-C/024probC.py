import sys
input = sys.stdin.readline

Alp = [chr(i) for i in range(97, 97+26)]

N, K = map(int, input().split())
S = input().rstrip()

dic = {}
for k in range(K):
    if S[k] in dic:
        dic[S[k]] += 1
    else:
        dic[S[k]] = 1

def dictokey(dic):
    key = ""
    for a in Alp:
        if not a in dic or dic[a] == 0:
            continue
        key += a + str(dic[a])
    return key

keys = [dictokey(dic)]
for i in range(N-K):
    dic[S[i]] -= 1
    s = S[i+K]
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
    keys.append(dictokey(dic))

ansdic = {}
ans = False
for i, key in enumerate(keys):
    if key in ansdic:
        if i - ansdic[key] >= K:
            ans = True
            break
    else:
        ansdic[key] = i

print("YES" if ans else "NO")