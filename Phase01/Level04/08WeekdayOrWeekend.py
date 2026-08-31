
"""
Question 8:
Take a weekday number (1-7) and determine if it is a
weekday or weekend.

Explanation:
- Numbers 1 to 5 represent weekdays.
- Numbers 6 and 7 represent weekends.
- If the input is between 1 and 7, determine whether it is
  a weekday or weekend.
- Otherwise, print "Invalid Day".

Test Cases:
Input  : 1
Output : Weekday

Input  : 5
Output : Weekday

Input  : 6
Output : Weekend

Input  : 7
Output : Weekend

Input  : 8
Output : Invalid Day
"""

n=int(input("Enter :  "))


if 1<=n<7:
    if 1<=n<=5:
        print("Weekdays")
    else:
        print("Weekends")
else:
    print("invalid day")
