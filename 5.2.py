total=0
count=0
max=None
min=None
while True :
    num = raw_input("Enter a number:")
    if num == "done":
        break
    else:
        try : 
            Num=int(num) 
            total=total+Num
            count=count+1
        except:
            print "Invalid input"
            continue
    if max is None :
        max = num
    elif num > min : 
        max = num
    if min is None :
        min = num
    elif num < min : 
        mint = num
print total, count, max, min
