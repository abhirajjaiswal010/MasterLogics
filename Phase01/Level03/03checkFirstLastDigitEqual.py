'''
Question 3:

Take a 4-digit number and check if the first and last digits are equal.

Example 1:
Input: 1221
Output: First and last digits are equal

Example 2:
Input: 1234
Output: First and last digits are not equal
'''


s=input("Enter The digit :")

if s[0]==s[len(s)-1]:
    print("equal")
else:
    print("not equal ")