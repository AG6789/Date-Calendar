#Import Date-Time
from datetime import date, datetime

#Get today's date
day = date.today()
dateToday = day.strftime("%d/%m/%Y")
dayToday = datetime.today().weekday()
dateString = dateToday.split("/")
dateToday2 = date(int(dateString[2]), int(dateString[1]), int(dateString[0]))

#Month Variable
monthDays = []

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

#weekdays, months
dayName = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}        

month ={1:'January', 2:'February', 3:'March', 
        4:'April', 5:'May', 6:'June', 7:'July',
        8:'August', 9:'September', 10:'October',
        11:'November', 12:'December'}

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
dateInput = input("Please enter month in mm/yyyy format: ")
dayInputString = dateInput.split("/")
for x in range(1):
    dayInputString[x] = int(dayInputString[x])

#Error-Checks
if dayInputString[0] > 12 or dayInputString[0] < 1:
    print("Gotcha months wrong mate, sorry.")

#Date value
dayNow = dayDay(1, dayInputString[0], dayInputString[1])
if dayNow == 7:
    dayNow = 0

dayNow2 = dayDay(1, dayInputString[0], dayInputString[1])
if dayNow2 == 7:
    dayNow2 = 0
    
weekday = dayName[dayNow2]

#getting dates
if (dayInputString[0] == 1 or dayInputString[0] == 3 or dayInputString[0] == 5 or dayInputString[0] == 7 or dayInputString[0] == 8 or dayInputString[0] == 10 or dayInputString[0] == 12):
    for x in range(30):
        weekday = dayName[dayNow2]
        monthDays.append(weekday)
        dayNow2 += 1
        if dayNow2 == 7:
            dayNow2 = 0 

elif (dayInputString[0] == 4 or dayInputString[0] == 6 or dayInputString[0] == 9 or dayInputString[0] == 11):
    for x in range(29):
        weekday = dayName[dayNow2]
        monthDays.append(weekday)
        dayNow2 += 1
        if dayNow2 == 7:
            dayNow2 = 0 

elif (dayInputString[0] == 2):
    if (leapYear):
        for x in range(28):
            weekday = dayName[dayNow2]
            monthDays.append(weekday)
            dayNow2 += 1
            if dayNow2 == 7:
                dayNow2 = 0 
    else:
        for x in range(27):
            weekday = dayName[dayNow2]
            monthDays.append(weekday)
            dayNow2 += 1
            if dayNow2 == 7:
                dayNow2 = 0 
                
print(" ")
print("    ", month[dayInputString[0]], dayInputString[1])
print("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")

print(" - "*dayNow, end="")
count = dayNow + 1
for x in range(31):
    if count == 7:
        count = 0
        print("%02d" % (x+1,))
    
    else:
        print("%02d" % (x+1,), end=" ")
    count += 1
    
    
    

