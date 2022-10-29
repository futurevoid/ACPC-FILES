end = int(input(""))

for num in range(end + 1):
    if num%2 == 0:
        if num == 0:
            pass
        else:
            print(num, sep="")
            
if end==1:
   print("-1")