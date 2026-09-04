'''
02. Reverse a Number

Question:
Given an integer n, reverse its digits and print the resulting number.

Test Cases:
Input: 12345
Output: 54321

Input: 123
Output: 321

Input: 100
Output: 1

Input: 9876
Output: 6789
'''

n=int(input("Enter :"))
rev=0

while n>0:
    d=n%10
    rev=rev*10+d
    n//=10

print(rev)


