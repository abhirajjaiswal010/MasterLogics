'''
Question 8:

Check if a number lies within the range [100, 999].

Example 1:
Input: 150
Output: Number lies within the range

Example 2:
Input: 999
Output: Number lies within the range

Example 3:
Input: 1000
Output: Number does not lie within the range
'''

l,h=map(int,input("Enter The low and high : ").split())
n=int(input("Enter The Number : "))

if l<=n<=h:
    print("Number lies within the range")
else:
    print("Number do not lies")