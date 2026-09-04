'''
06. Check Perfect Number

Question:
Given an integer n, check whether it is a perfect number.

A perfect number is a positive integer that is equal to the sum
of its proper positive divisors.

Test Cases:
Input: 6
Output: Perfect Number

Input: 28
Output: Perfect Number

Input: 496
Output: Perfect Number

Input: 12
Output: Not Perfect Number

Example:
6 -> 1 + 2 + 3 = 6
'''

n=int(input("Enter : "))

sum=0
i=1
while n>i:
    if n%i==0:
        sum+=i
    i+=1

print(sum==n)
