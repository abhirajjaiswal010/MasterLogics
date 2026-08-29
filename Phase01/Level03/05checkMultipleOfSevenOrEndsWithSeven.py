'''
Question 5:

Check if a number is a multiple of 7 or ends with 7.

Example 1:
Input: 14
Output: Multiple of 7

Example 2:
Input: 27
Output: Ends with 7

Example 3:
Input: 35
Output: Multiple of 7

Example 4:
Input: 123
Output: Neither multiple of 7 nor ends with 7
'''

s=input("Enter The Number  : ")

if int(s)%7==0 :
    print("multiple")
if s[-1]==7:
    print("ends")
else:
    print("neither")
    