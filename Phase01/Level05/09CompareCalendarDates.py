'''
Docstring for Phase01.Level05.09CompareCalendarDates
9. Take two dates (day and month) and determine which date comes
   first in the calendar.

   Test Cases:
   Input:
   Date 1: 10 3
   Date 2: 15 3
   Output: Date 1 comes first

   Input:
   Date 1: 20 5
   Date 2: 10 4
   Output: Date 2 comes first

   Input:
   Date 1: 15 8
   Date 2: 15 8
   Output: Both dates are same

   Input:
   Date 1: 28 2
   Date 2: 1 3
   Output: Date 1 comes first
   '''
date1,month1 = map(int,(input("Enter Date: ")).split())
date2,month2 = map(int,(input("Enter Date: ")).split())


if month1==month2:
    if date1<date2:
        print("date 1 come first")
    elif date1==date2:
        print("Both date equal")
    else:
        print("date 2 come first")
elif month1<month2:
   print("date 1 comes first")

else:
    print("date2 come first")

    




      

