"""
07. SUM OF EVEN NUMBERS

Write a Python program to take a positive integer n as input
and print the sum of all even numbers from 1 to n.
"""

n=int(input("Enter Num : "))

if n>0:
    sum=0
    for i in range(1,n+1):
        if i%2==0:
            sum+=i
    print(f"sum of even num till {sum}")
else:
    print("num is negative")