'''
Question 7:

Check if an amount can be evenly divided into 2000, 500, and
100 currency notes.

Example 1:
Input: 5000
Output: Amount can be evenly divided into 2000, 500, and 100 notes

Example 2:
Input: 3500
Output: Amount can be evenly divided into 2000, 500, and 100 notes

Example 3:
Input: 3550
Output: Amount cannot be evenly divided into 2000, 500, and 100 notes
'''

s = int(input("Enter the Amount: "))

r1 = s % 2000
q1 = s // 2000

r2 = r1 % 500
q2 = r1 // 500

if r2 % 100 == 0:
    print("The amount can be divided into ₹2000, ₹500, and ₹100 notes.")
else:
    print("The amount cannot be divided into ₹2000, ₹500, and ₹100 notes.")
