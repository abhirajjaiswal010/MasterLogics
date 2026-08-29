'''
Question 4:

Check whether a given integer is single-digit, double-digit, or
multi-digit.

Example 1:
Input: 7
Output: Single-digit

Example 2:
Input: 45
Output: Double-digit

Example 3:
Input: 1234
Output: Multi-digit
'''


s=input("Enter The Num : ")

if len(s)==1:
    print("single")
elif len(s)==2:
    print("double")
else:
    print("multi")