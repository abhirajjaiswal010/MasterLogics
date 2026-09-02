'''
Docstring for Phase01.Level05.03ValidCalendarDate
3. Take day and month and check if they form a valid calendar date.
   Ignore leap years.

   Test Cases:
   Input: 15 8
   Output: Valid Date

   Input: 31 4 april -> 30
   Output: Invalid Date

   Input: 28 2
   Output: Valid Date

   Input: 29 2
   Output: Invalid Date

   Input: 15 13
   Output: Invalid Date
'''
# jsan -> june spet april nov -> 30 

day,month=map(int,input("Enter Day and Month  :").split())

if 1<=month<=12:
    if month==2:
        if 1<=day<=28:
            print("valid date")
        else:
            print("invalid date")

    elif month in [4,6,9,11]:
        if 1<=day<=30:
            print("valid Date")
        else:
            print("invalid Date")

    else:
        if 1<=day<=31:
            print("valid Date")
        else:
            print("invalid Date")
            
else:
    print("Month Is Not Valid")

