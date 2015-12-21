hours=raw_input("How many hours do you work per week?\n")
try: 
    Hours = float(hours)
    rate=raw_input("How much do you get paid per hour?\n")
    try: 
        Rate = float(rate)
        if Hours < 40 :
            TotalPay=float(Hours)* float(Rate)
            print "So, you get paid " + str(TotalPay) + " per week?" 
        else:
            TotalPay=(float(Hours)-40)*1.5*float(Rate)+40*float(Rate)
            print "So, you get paid " + str(TotalPay) + " dollars per week?"
    except: 
        Rate = -1
    if Rate <0 :
        print "Please enter numeric input!"
except: 
    Hours = -1
if Hours <0 :
    print "Please enter numeric input!"
