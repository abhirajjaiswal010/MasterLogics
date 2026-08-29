'''
Question 10:

Check whether a number is a perfect square without using the
square root function.

Example 1:
Input: 25
Output: Perfect square

Example 2:
Input: 36
Output: Perfect square

Example 3:
Input: 20
Output: Not a perfect square

Example 4:
Input: 1
Output: Perfect square
'''

s=int(input("Enter The NUmber : "))
t=s
sum=0

while True:
    innersum=0
    i=0
    while s>0:
        d=s%10
        innersum+=d
        s//=10
        i+=1
    
    if '0'<str(innersum)<'9':
        sum=innersum
        break
    else:
        s=innersum


if str(sum) in "1479":
    print("Sq perfect")
else:
    print("not sq perfect")

    

