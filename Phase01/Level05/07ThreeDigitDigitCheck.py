'''
Docstring for Phase01.Level05.07ThreeDigitDigitCheck
7. Take a 3-digit number and check if the sum of the first and last
   digit is equal to the middle digit.

   Test Cases:
   Input: 121
   Output: True

   Input: 132
   Output: True

   Input: 123
   Output: False

   Input: 352
   Output: True

   Input: 999
   Output: False
'''

a=int(input("Enter the numbers : "))

first=a//100
mid=(a%100)//10
last=a%10
sum = first+last
if sum==mid:
    print("True")
else:
    print("False")



