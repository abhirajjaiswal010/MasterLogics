'''
Question:
Write a Python program to print all factors of a given number.

Test Case:
Input:
24

Output:
1 2 3 4 6 8 12 24
'''
n=int(input("Enter : "))

for i in range(1,n+1):
    if n%i==0:
        print(i)