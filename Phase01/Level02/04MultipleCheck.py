'''
Question:
Take two numbers and check whether one number is a multiple of the other.

Test Cases:

Input: 10 5
Output: Multiple

Input: 15 4
Output: Not a Multiple

Input: 7 21
Output: Multiple
'''

n1,n2=map(int,input("Enter The Two Number  : ").split())

if n1%n2==0 or n2%n1==0:
    print("Multiple")
else:
    print("Not a Multiple")
