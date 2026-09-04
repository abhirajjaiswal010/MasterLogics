'''
01. Count the Number of Digits

Question:
Given an integer n, count and print the total number of digits present in the number.

Test Cases:
Input: 12345
Output: 5

Input: 789
Output: 3

Input: 5
Output: 1

Input: 1000
Output: 4
'''
n=int(input("Enter :"))

i=0 
while n>0:
    i+=1
    n//=10

print(i)