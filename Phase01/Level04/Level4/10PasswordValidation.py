
"""
Question 10:
Take a password string and check basic rules
(length >= 8 and contains at least one digit).

Explanation:
- The password must contain at least 8 characters.
- The password must contain at least one digit (0-9).
- If both conditions are satisfied, print "Valid Password".
- Otherwise, print "Invalid Password".

Test Cases:
Input  : Python123
Output : Valid Password

Input  : Python
Output : Invalid Password

Input  : Password1
Output : Valid Password

Input  : Pass123
Output : Invalid Password
"""

password=input("Enter The Pass : ")
digit=0


if len(password)>=8:
    for i in password:
        if '0'<i<'9':
            digit=1
        if digit==1:
            print("Valid Password")
            break
else:
    print("Invalid Password")
    
