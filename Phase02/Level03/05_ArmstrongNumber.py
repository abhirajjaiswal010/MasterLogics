'''
05. Check Armstrong Number

Question:
Given an integer n, check whether it is an Armstrong number.

For a number having k digits, calculate the sum of each digit raised
to the power k. If the sum is equal to the original number,
the number is an Armstrong number.

Test Cases:
Input: 153
Output: Armstrong

Input: 370
Output: Armstrong

Input: 9474
Output: Armstrong

Input: 123
Output: Not Armstrong
'''

n=int(input("Enter :"))
pow=len(str(n))
temp=n
sum=0
while n>0:
    d=n%10
    sum+=d**pow
    n//=10

print(temp==sum)

