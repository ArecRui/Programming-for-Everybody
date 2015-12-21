Hours=raw_input("How many hours do you work per week?\n")
Rate=raw_input("How much do you get paid per hours?\n")

if Hours < 40 :
    TotalPay=float(Hours)* float(Rate)
    print "So, you get paid " + str(TotalPay) + " per week?" 
else :
    TotalPay=(float(Hours)-40)*1.5*float(Rate)+40*float(Rate)
    print "So, you get paid " + str(TotalPay) + " per week?"
