
"""
Question 11:
Take 24-hour time (hours and minutes) and print whether
it is AM or PM.

Explanation:
- If the hour is between 0 and 11, it is AM.
- If the hour is between 12 and 23, it is PM.
- The hour must be between 0 and 23.
- The minutes must be between 0 and 59.

Test Cases:
Input  : 10 30
Output : AM

Input  : 12 00
Output : PM

Input  : 18 45
Output : PM

Input  : 23 59
Output : PM

Input  : 25 10
Output : Invalid Time
"""

hrs,min=map(int,input("Enter The Time IN HH:MM ->").split(":"))

if 0<=hrs<=24 and 0<=min<60:
    if 0<=hrs<=11:
        print("AM")
    else:
        print("PM")
else:
    print("Invalid Time")
