import sys
input = sys.stdin.readline

Alp = [chr(i) for i in range(97, 97+26)]

N = int(input())
S = input().rstrip()
ans = 0
for a in reversed(Alp):
    while True:
        update = False
        for i in range(len(S)):
            if S[i] != a: continue
            if i != 0 and ord(S[i-1]) == ord(a) - 1:
                S = S[:i] + S[i+1:]
                update = True
                break
            if i != len(S)-1 and ord(S[i+1]) == ord(a) - 1:
                S = S[:i] + S[i+1:]
                update = True
                break
        if not update:
            break
        ans += 1

print(ans)