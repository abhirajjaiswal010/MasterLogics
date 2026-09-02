'''
Docstring for Phase01.Level05.08DigitSumVsProduct
8. Take an integer between 1 and 9999 and check whether the sum
   of its digits is greater than the product of its digits.

   Test Cases:
   Input: 123
   Output: False

   Input: 111
   Output: True

   Input: 105
   Output: True

   Input: 999
   Output: False

   Input: 1000
   Output: True
'''
n = int(input("Enter Number: "))
sum=0
pro=1

while n>0:
    d = n%10
    sum+=d
    pro*=d
    n//=10
print("Sum is = ",sum)
print("product is = ",pro)

if sum > pro:
    print("True")
else:
    print("False")



    

    


        



