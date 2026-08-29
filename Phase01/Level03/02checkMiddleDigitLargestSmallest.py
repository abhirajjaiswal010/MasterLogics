'''
Question 2:

Take a 3-digit number and determine if the middle digit is the
largest, smallest, or neither.

Example 1:
Input: 132
Output: Middle digit is the largest

Example 2:
Input: 213
Output: Middle digit is the smallest

Example 3:
Input: 321
Output: Middle digit is neither the largest nor the smallest
'''
s=input("Enter The number : ")
i=len(s)//2

if s[i-1]<s[i] and s[i]>s[i+1]:
    print("large")
elif s[i-1]>s[i] and s[i]<s[i+1]:
    print("small")
else:
    print("neither large nor small")
