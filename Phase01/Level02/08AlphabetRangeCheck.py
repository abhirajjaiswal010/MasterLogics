'''
Question:
Take an alphabet character and check whether it lies between 'a' and 'm'
or between 'n' and 'z'.

Test Cases:

Input: g
Output: Between a and m

Input: t
Output: Between n and z

Input: m
Output: Between a and m
'''

s=input("Enter The String  : ").lower()


if "a"<=s<="m":
    print("btw a and m")
else:
    print("btw n and z ")