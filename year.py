from datetime import date
todays_date=date.today()
print("current date:",todays_date)
print ("current year:",todays_date.year)
a=int(input("enter a year:"))
for i in range(todays_date.year,a):
    if (i %400==0)or(i %100==0):
        print ("{0} is a leap year".format(i))
    elif(i%4==0) and (i%100!=0):
         print("{0} is a leap year".format(i))
    
 

 
