N = int(input())
S = input()

Alp = [chr(i) for i in range(65, 65+26)]
A = 'ACTG'

ans = 10**12
for i in range(N-3):
    T = S[i:i+4]
    score = 0
    for j in range(4):
        s1 = Alp.index(A[j])
        t1 = Alp.index(T[j])
        score += min([abs(s1-t1), abs(s1-t1-26), abs(s1-t1+26)])
    ans = min(ans, score)
print(ans)
