import sys
input = sys.stdin.readline

S = input().rstrip()


# アルファベット小文字
alp = [chr(i) for i in range(97, 97+26)]
# 大文字
Alp = [chr(i) for i in range(65, 65+26)]

Words = []
w = ""
for s in S:
    if 97 <= ord(s) < 97+26:
        w += s
    else:
        if not w:
            w += s.lower()
        else:
            w += s.lower()
            Words.append(w)
            w = ""

Words.sort()
for word in Words:
    nword = word[0].upper() + word[1:-1] + word[-1].upper()
    print(nword, end="")
print()