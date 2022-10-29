n = input("")
n = int(n)
try:
    for n in range(n):
        print(n+1,sep="")
except ValueError:
    print("Not a Number")