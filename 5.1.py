total=0
count=0
average=0.0
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
average=float(total)/float(count)
print total, count, average
