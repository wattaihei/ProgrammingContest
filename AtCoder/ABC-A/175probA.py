S = input()
if S == "RRR":
    ans = 3
elif S == "RRS" or S == "SRR":
    ans = 2
elif "R" in S:
    ans = 1
else:
    ans = 0
print(ans)