"""
10. PRODUCT OF DIGITS

Write a Python program to take an integer as input
and print the product of all its digits.
"""

n=int(input("Enter Num : "))

i=0
pro=1
while n>0:
    d=n%10
    pro*=d
    n//=10
    i+=1

print(f"product of digit :  {pro}")