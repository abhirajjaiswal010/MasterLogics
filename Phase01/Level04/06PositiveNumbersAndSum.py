
"""
Question 6:
Take two numbers and check if both are positive and their
sum is less than 100.

Explanation:
- Both numbers must be greater than 0.
- Their sum must be less than 100.
- If both conditions are true, print "Valid".
- Otherwise, print "Invalid".

Test Cases:
Input  : 20 30
Output : Valid

Input  : 50 60
Output : Invalid

Input  : -10 20
Output : Invalid
"""

a,b=map(int,input("Enter The N1 and N2 : ").split())


if a>0 and b>0:
    if a+b<100:
        print("valid")
    else:
        print("Invalid")
else:
    print("Invalid")