'''
Question:
Write a Python program to print all numbers between a and b that are divisible by 7.

Test Case:
Input:
10
50

Output:
14 21 28 35 42 49
'''

a,b=map(int,input("Enter A and B : ").split())

for i in range(a,b+1):
    if i%7==0:
        print(i)