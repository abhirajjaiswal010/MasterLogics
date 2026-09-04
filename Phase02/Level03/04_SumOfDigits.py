'''
04. Sum of Digits

Question:
Given an integer n, calculate and print the sum of all its digits.

Test Cases:
Input: 12345
Output: 15

Input: 123
Output: 6

Input: 999
Output: 27

Input: 1000
Output: 1
'''

n=int(input("Enter : "))
sum=0
while n>0:
    d=n%10
    sum+=d
    n//=10

print(sum)
