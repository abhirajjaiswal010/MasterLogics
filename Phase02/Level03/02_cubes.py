'''
Question:
Write a Python program to print the cubes of all numbers from 1 to n.

Test Case:
Input:
5

Output:
1 8 27 64 125
'''

n=int(input("Enter : "))
for i in range(1,n+1):
    print(i**3)