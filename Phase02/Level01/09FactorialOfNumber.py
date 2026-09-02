"""
09. FACTORIAL OF A NUMBER

Write a Python program to take a non-negative integer as input
and print its factorial.
"""

n=int(input("Enter Num : "))

if n>0:
    pro=1
    for i in range(1,n+1):
        pro*=i
    print(f"Factorial of  num  {pro}")
else:
    print("num is negative")