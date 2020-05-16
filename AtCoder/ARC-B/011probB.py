
Alp = ["zr", "bc", "dw", "tj", "fq", "lv", "sx", "pm", "hk", "ng"]

N = int(input())
Ss = list(input().split())

ans = []
for S in Ss:
    T = S.lower()
    B = []
    for t in T:
        for i in range(10):
            if t in Alp[i]:
                B.append(str(i))
                break
    if B:
        ans.append("".join(B))

print(" ".join(ans))