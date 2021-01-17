X, Y = map(int, input().rstrip().split())

if Y == 0:
    print("ERROR")
else:
    s = str(100*X//Y)
    n = len(s)
    if n >= 3:
        ans = s[:n-2] + "." + s[n-2:]
    elif n == 2:
        ans = "0." + s
    else:
        ans = "0.0" + s
    print(ans) 
