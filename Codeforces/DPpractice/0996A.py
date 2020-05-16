N = int(input())
s = N//100 + (N%100)//20 + (N%20)//10 + (N%10)//5 + N%5
print(s)