
N = int(input())
S = input()

ALP = [chr(i) for i in range(65, 65+26)]
A = ALP + ALP
ans = ""
for s in S:
    ind = A.index(s)
    ans += A[ind+N]
print(ans)