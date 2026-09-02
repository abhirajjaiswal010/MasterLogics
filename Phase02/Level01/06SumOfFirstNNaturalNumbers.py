"""
06. SUM OF FIRST N NATURAL NUMBERS

Write a Python program to take a positive integer n as input
and print the sum of the first n natural numbers.
"""


n=int(input("Enter Num : "))

if n>0:
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(f"sum of natural num till {sum}")
else:
    print("num is negative")