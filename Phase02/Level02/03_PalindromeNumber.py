'''
03. Check Palindrome Number

Question:
Given an integer n, check whether the number reads the same from left to right
and right to left.

Print "Palindrome" if the number is a palindrome.
Otherwise, print "Not Palindrome".

Test Cases:
Input: 121
Output: Palindrome

Input: 1331
Output: Palindrome

Input: 123
Output: Not Palindrome

Input: 100
Output: Not Palindrome
'''

n=int(input("Enter :"))
rev=0
temp=n

while n>0:
    d=n%10
    rev=rev*10+d
    n//=10

print(rev==temp)