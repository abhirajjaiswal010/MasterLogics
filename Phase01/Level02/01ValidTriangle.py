'''
Question:
Take three sides of a triangle and check whether they can form a valid triangle.

Test Cases:

Input: 3 4 5
Output: Valid Triangle

Input: 1 2 3
Output: Invalid Triangle

Input: 5 5 5
Output: Valid Triangle
'''

a,b,c=map(int,input("Enter The Three Side : ").split())

if a+b>c and b+c>a and c+a>b:
    print("valid trianlge")
else:
    print("Invalid Triangle")