#Import Date-Time
from datetime import date, datetime
#Get today's date
day = date.today()
dateToday = day.strftime("%d/%m/%Y")
dayToday = datetime.today().weekday()
dateString = dateToday.split("/")
dateToday2 = date(int(dateString[2]), int(dateString[1]), int(dateString[0]))

#Leap-Year Check
def leapYear(y):
    if (y%400 == 0):
        return True
    elif (y%4 == 0 and y%100 != 0):
        return True
    elif (y%4 != 0):
        return False
    elif (y%100 == 0 and y%400 != 0):
        return False

#Weeday Into - Name
dayName = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}        

#Integer Name for Weekday
def dayDay(d, m, y):
    
    newDate = date(int(y), int(m), int(d))
    dateDiff = (newDate - dateToday2).days
    dateDiffAbs = abs(dateDiff)
    dayDiff1 = dateDiffAbs%7    
    
    if dateDiff >= 0:
        dayNow = dayDiff1 + dayToday
    else:
        if dayToday > dayDiff1:
            dayNow = dayToday-dayDiff1
        else:
            dayDiff1 = 7-dayDiff1
            dayNow = dayToday - dayDiff1
    
    return dayNow

#Input date
dateInput = input("Please enter date in dd/mm/yyyy format: ")
dayInputString = dateInput.split("/")
for x in range(2):
    dayInputString[x] = int(dayInputString[x])

#Error-Checks
if dayInputString[1] > 12 or dayInputString[1] < 1:
    print("Gotcha months wrong mate, sorry.")
if(dayInputString[1] == 4 or dayInputString[1] == 6 or dayInputString[1] == 9 or dayInputString[1] == 11):
    if(dayInputString[0] > 30 or dayInputString[0] < 1):
        print("Gotcha days wrong mate ;)")     
elif (dayInputString[1] == 2):
    if (leapYear(dayInputString[2])):
        if(dayInputString[0] > 29 or dayInputString[0] < 1):
            print("Gotcha days wrong mate ;)")
    elif (dayInputString[0] > 28 or dayInputString[0] < 1):
        print("Gotcha days wrong mate ;)")
else:
    if(dayInputString[0] > 31 or dayInputString[0] < 1):
        print("Gotcha days wrong mate ;)")

#Final values and Output
dayNow = dayDay(dayInputString[0], dayInputString[1], dayInputString[2])
if dayNow == 7:
    dayNow = 0
    
weekday = dayName[dayNow]
print("\n")
print(f"{dateInput} will be/was a {weekday}.")

   


    

    
    
    

