hours=raw_input("How many hours do you work per week?\n")
try: 
    Hours = int(hours)
except: 
    Hours = -1
rate=raw_input("How much do you get paid per hours?\n")
try: 
    Rate = int(rate)
except: 
    Rate = -1
if Hours <0 or Rate <0:
    print "Please enter a number(i.e. 8 10)!"
elif Hours < 40 :
    TotalPay=int(Hours)* int(Rate)
    print "So, you get paid " + str(TotalPay) + " per week?" 
else:
    TotalPay=(int(Hours)-40)*1.5*int(Rate)+40*int(Rate)
    print "So, you get paid " + str(TotalPay) + " dollars per week?"
